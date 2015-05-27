import util


class TestESGD:
    def test_rosen(self):
        util.assert_progress(*util.build_rosen('esgd'))

    def test_factor(self):
        util.assert_progress(*util.build_factor('esgd'))


class TestRProp:
    def test_rosen(self):
        util.assert_progress(*util.build_rosen('rprop'))

    def test_factor(self):
        util.assert_progress(*util.build_factor('rprop'))


class TestRMSProp:
    def test_rosen(self):
        util.assert_progress(*util.build_rosen('rmsprop'))

    def test_factor(self):
        util.assert_progress(*util.build_factor('rmsprop'))


class TestADADELTA:
    def test_rosen(self):
        util.assert_progress(*util.build_rosen('adadelta'))

    def test_factor(self):
        util.assert_progress(*util.build_factor('adadelta'))