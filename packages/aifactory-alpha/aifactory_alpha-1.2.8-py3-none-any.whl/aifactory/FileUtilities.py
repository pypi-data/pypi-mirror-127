import os
import shutil

ROOT_DIR = '/mnt/SUBMISSIONS/'
ARCHIVE_DIR = '/mnt/ARCHIVES/'
MAX_SUB_SAVE = 1
EXPECTED_MAXIMUM_SUBMISSION_DIGITS = 4

TASK_DIR_PREFIX = 'TASK_ID'
LAP_DIR_PREFIX = 'LAP'
USER_DIR_PREFIX = 'USER_ID'
SUBMISSION_DIR_PREFIX = 'SUB'

SCRIPT_DIR_PREFIX = 'SCRIPT'
GTANSWER_DIR_PREFIX = 'GTANSWER'
BEST_DIR_NAME = 'BEST'


def get_task_directory(task_id, root_dir=ROOT_DIR):
    # check if task_id root directory exists
    task_dir = os.path.join(root_dir, '{}_{}'.format(TASK_DIR_PREFIX, task_id))
    if not os.path.exists(task_dir):
        os.makedirs(task_dir)
    return task_dir


def get_lap_directory(task_id, lap_num, root_dir=ROOT_DIR):
    task_dir = get_task_directory(task_id, root_dir=root_dir)
    # check if task_id/lap root directory exists
    lap_dir = os.path.join(task_dir, '{}_{}'.format(LAP_DIR_PREFIX, lap_num))
    if not os.path.exists(lap_dir):
        os.makedirs(lap_dir)
    return lap_dir


def archive_lap(task_id, lap_num, root_dir=ROOT_DIR):
    pass

def clear_lap(task_id, lap_num, root_dir=ROOT_DIR):
    pass

def get_user_directory(task_id, lap_num, user_id, root_dir=ROOT_DIR):
    """

    :param task_id:
    :param lap_num:
    :param user_id:
    :return:
    >>> get_user_directory(0, 0, 'test@aifactory.page', root_dir='./')
    './task_id_0/lap_0/user_id_test@aifactory.page'
    """
    # should be simplified later.
    lap_dir = get_lap_directory(task_id, lap_num, root_dir=root_dir)
    user_dir = os.path.join(lap_dir, '{}_{}'.format(USER_DIR_PREFIX, user_id))
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
        # first submission
    return user_dir


def get_submission_directory(task_id, lap_num, user_id, num_submission: int, if_exist=True,
                             root_dir=ROOT_DIR):
    user_dir = get_user_directory(task_id, lap_num, user_id, root_dir=root_dir)
    submission_tail = str(num_submission).zfill(EXPECTED_MAXIMUM_SUBMISSION_DIGITS)
    sub_dir = os.path.join(user_dir, '{}_{}'.format(SUBMISSION_DIR_PREFIX, submission_tail))
    if if_exist and (not os.path.exists(sub_dir)):
        return None
    return sub_dir


def get_best_directory(task_id, lap_num, user_id, root_dir=ROOT_DIR):
    """
    :param task_id:
    :param lap_num:
    :param user_id:
    :param num_submission:
    :return:

    >>> get_best_directory(0, 0, 'test@aifactory.page', root_dir='./')
    './TASK_ID_0/LAP_0/USER_ID_test@aifactory.page/BEST'
    """
    user_dir = get_user_directory(task_id, lap_num, user_id, root_dir=root_dir)
    best_dir = os.path.join(user_dir, BEST_DIR_NAME)
    if not os.path.exists(best_dir):
        os.makedirs(best_dir)
    return best_dir


def get_latest_directory(task_id, lap_num, user_id, root_dir=ROOT_DIR):
    """

    :param task_id:
    :param lap_num:
    :param user_id:
    :return:

    >>> get_new_directory(0, 0, 'test@aifactory.page', root_dir='./')
    './TASK_ID_0/LAP_0/USER_ID_test@aifactory.page/SUB_0001'
    >>> get_latest_directory(0, 0, 'test@aifactory.page', root_dir='./')
    './TASK_ID_0/LAP_0/USER_ID_test@aifactory.page/SUB_0001'
    """
    user_dir = get_user_directory(task_id, lap_num, user_id, root_dir=root_dir)
    past_submissions = os.listdir(user_dir)
    past_submissions = [(sub, int(sub[-EXPECTED_MAXIMUM_SUBMISSION_DIGITS:])) \
                        for sub in past_submissions if sub.startswith(SUBMISSION_DIR_PREFIX)]
    if len(past_submissions) == 0:
        return None
    past_submissions.sort(key=lambda x: x[1])
    past_submissions.sort()
    return os.path.join(user_dir, past_submissions[-1][0])


def get_new_directory(task_id, lap_num, user_id, cur_num_submission=None, root_dir=ROOT_DIR):
    if type(cur_num_submission) != int:
        cur_num_submission = None
    # should be simplified later.
    user_dir = get_user_directory(task_id, lap_num, user_id, root_dir=root_dir)
    past_submissions = os.listdir(user_dir)
    past_submissions = [(sub, int(sub[-EXPECTED_MAXIMUM_SUBMISSION_DIGITS:])) \
                        for sub in past_submissions if sub.startswith(SUBMISSION_DIR_PREFIX)]
    if len(past_submissions) == 0 and (cur_num_submission is None):
        cur_num_submission = 1
    past_submissions.sort(key=lambda x: x[1])
    if len(past_submissions) > MAX_SUB_SAVE:
        for old_sub, _ in past_submissions[:-MAX_SUB_SAVE]:
            shutil.rmtree(os.path.join(user_dir, old_sub), ignore_errors=True)
    latest_file_dir = get_submission_directory(task_id, lap_num, user_id,
                                               num_submission=cur_num_submission,
                                               if_exist=False, root_dir=root_dir)
    os.makedirs(latest_file_dir, exist_ok=True)
    return latest_file_dir


def get_script_directory(task_id=None, lap_num=None, root_dir=ROOT_DIR):
    """

    :param task_id:
    :param lap_num:
    :return:

    >>> get_script_directory(0, 0, root_dir='./')
    './TASK_ID_0/LAP_0/SCRIPT'
    """
    lap_dir = get_lap_directory(task_id, lap_num, root_dir=root_dir)
    script_dir = os.path.join(lap_dir, SCRIPT_DIR_PREFIX)
    if not os.path.exists(script_dir):
        os.makedirs(script_dir)
    return script_dir


def get_answer_directory(task_id=None, lap_num=None, root_dir=ROOT_DIR):
    """

    :param task_id:
    :param lap_num:
    :return:

    >>> get_answer_directory(0, 0, root_dir='./')
    './TASK_ID_0/LAP_0/GTANSWER'
    """
    lap_dir = get_lap_directory(task_id, lap_num, root_dir=root_dir)
    answer_dir = os.path.join(lap_dir, GTANSWER_DIR_PREFIX)
    if not os.path.exists(answer_dir):
        os.makedirs(answer_dir)
    return answer_dir
