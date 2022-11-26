from apscheduler.schedulers.background import BackgroundScheduler

import config
from _logging import logger as log
from util import write_to_file, read_from_file, get_totp_token

def task():
    log.debug('Generating TOTP...')
    totp = get_totp_token(config.SECRET)
    write_to_file(totp, config.FILENAME)
    log.debug(f'Wrote new TOTP [{totp}] to file.')

def set_background_update():
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(task, 'interval', seconds=config.INTERVAL)
    job.func()
    scheduler.start()


def validate(user_code):
    totp = read_from_file(config.FILENAME)
    return user_code == totp



def login():
    while True:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')

        if username == config.CREDENTIALS['username'] and password == config.CREDENTIALS['password']:
            break
        else:
            print('Invalid credentials. Please, try again.')



if __name__ == '__main__':
    set_background_update()
    login()
    entered_code = input('Enter verification code: ')
    while not validate(entered_code):
        entered_code = input('Wrong code. Please try again: ')

    print('Logged in successfully!')
