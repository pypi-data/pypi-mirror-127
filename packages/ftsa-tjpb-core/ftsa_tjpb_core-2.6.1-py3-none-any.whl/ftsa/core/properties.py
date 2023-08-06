PACKAGE_NAME            = 'ftsa-tjpb-core'
SLEEP_SECONDS           = 5
REMOTE_VERSION          = '4.1.0-prerelease-20211105'
REC_VIDEO_VERSION       = 'ffmpeg-4.3.1-20211105'
VERSION                 = '2.6.1'
TEST_PYPI               = False

FTSA_SELENIUM_LIB_NAME  = 'FTSASeleniumLibrary'
FTSA_SSH_LIB_NAME       = 'FTSASSHLibrary'
FTSA_DATABASE_LIB_NAME  = 'FTSADatabaseLibrary'
FTSA_APPIUM_LIB_NAME    = 'FTSAAppiumLibrary'
FTSA_REQUESTS_LIB_NAME  = 'FTSARequestsLibrary'

DEPENDENCIES = [
    'robotframework',
    'robotframework-seleniumlibrary',
    'robotframework-sshlibrary',
    'robotframework-databaselibrary',
    'robotframework-appiumlibrary',
    'robotframework-requests',
    'robotframework-faker',
    'selenium',
    'webdrivermanager',
    'docker',
    'setuptools',
    'wheel',
    'twine'
]
