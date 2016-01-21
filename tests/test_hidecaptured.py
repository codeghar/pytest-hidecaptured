# -*- coding: utf-8 -*-


def test_assert_false(testdir):
    """Test pytest does not display captured stderr on test failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def test_logging():
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert False
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr call" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout call" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


def test_assert_true(testdir):
    """Test pytest does not display captured stderr on test failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def test_logging():
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr and stdout is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr call" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout call" not in line

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_setup_assert_false(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def setup_module(module):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert False


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr setup" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout setup" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


def test_setup_assert_true(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def setup_module(module):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert True


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr setup" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout setup" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 0


def test_setup_function_assert_false(testdir):
    """Test pytest does not display captured stderr on test setup function failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def setup_function(function):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert False


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr setup" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout setup" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


def test_setup_function_assert_true(testdir):
    """Test pytest does not display captured stderr on test setup function failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def setup_function(function):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert True


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()
    # print(result.stdout.lines)

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr setup" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout setup" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 0


def test_teardown_assert_false(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def teardown_module(module):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert False


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr teardown" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout teardown" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


def test_teardown_assert_true(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def teardown_module(module):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert True


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr teardown" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout teardown" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 0


def test_teardown_function_assert_false(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def teardown_function(function):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert False


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr teardown" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout teardown" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1


def test_teardown_function_assert_true(testdir):
    """Test pytest does not display captured stderr on test setup failure."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        import sys
        import datetime
        import logging
        import logging.handlers

        log_format = '%(asctime)s : %(name)s : %(module)s : %(funcName)s : %(levelname)s : %(message)s'
        formatter = logging.Formatter(fmt=log_format)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        strftime_format = '%Y%m%d-%H%M%S'
        file_name = '{0}-{1}.log'.format(__name__, datetime.datetime.utcnow().strftime(strftime_format))
        file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=1000, backupCount=5)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        def teardown_function(function):
            print('PRINT DEBUG!')
            logger.debug('DEBUG!')
            logger.info('INFO!')
            logger.warning('WARNING!')
            logger.error('ERROR!')
            logger.critical('CRITICAL!')
            assert True


        def test_logging():
            assert True
    """)

    # run pytest with no cmd args
    result = testdir.runpytest()

    # Assert captured stderr is not displayed
    for line in result.stdout.lines:
        assert "Captured stderr teardown" not in line
        assert "test_logging : DEBUG : DEBUG!" not in line
        assert "test_logging : INFO : INFO!" not in line
        assert "test_logging : WARNING : WARNING!" not in line
        assert "test_logging : ERROR : ERROR!" not in line
        assert "test_logging : CRITICAL : CRITICAL!" not in line
        assert "Captured stdout teardown" not in line

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 0
