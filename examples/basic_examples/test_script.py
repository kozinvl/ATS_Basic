import logging
from ats import aetest

log = logging.getLogger(__name__)


class common_setup(aetest.CommonSetup):

    @aetest.subsection
    def subsection_one(self):
        log.info('In Common Setup')
        log.info('preparing execute tests')

    @aetest.subsection
    def subsection_two(self, section):
        log.info('Doing something another')
        log.info("inside %s" % (section))


class Testcase_One(aetest.Testcase):

    @aetest.setup
    def setup(self):
        log.info("%s Setup/Preparation" % self.uid)
        self.a = 1
        self.b = 2
        self.c = 3

    @aetest.test
    def test_one(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        assert self.a == 1

    @aetest.test
    def test_two(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        assert self.b == 2

    @aetest.test
    def test_three(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        assert self.c == 3

    @aetest.test
    def test_assert(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        assert self.b == 23

    @aetest.test
    def test_skipped(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        self.skipped('this test was skipped')

    @aetest.test
    def test_blocked(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        self.blocked('this test was blocked')

    @aetest.test
    def test_errored(self, section):
        log.warning("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        self.errored('this test was errored')

    @aetest.test
    def test_aborted(self, section):
        log.info("Execute Test section: %s in testcase %s" % (section.uid, self.uid))
        self.aborted('this test was aborted')


class common_cleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean_everything(self):
        log.info('In Common Cleanup')
        log.info('Finish')


if __name__ == '__main__':
    aetest.main()
