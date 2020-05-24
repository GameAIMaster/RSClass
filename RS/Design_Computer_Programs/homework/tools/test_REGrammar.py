import sys
import unittest
import Design_Computer_Programs.homework.tools.REGrammar as hw

REGRAMMAR = hw.REGRAMMAR
parse = hw.parse
parse_re = hw.parse_re
FAIL = (None, None)


class Test(unittest.TestCase):
    def test_eol(self):
        result = parse('eol', '', REGRAMMAR)
        answer = (['eol', ''], '')
        print(result)
        self.assertEqual(result, answer)

        result = parse('eol', 'a', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

    def test_dot(self):
        result = parse('dot', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('dot', '.', REGRAMMAR)
        answer = (['dot', '.'], '')
        self.assertEqual(result, answer)

    def test_lit(self):
        result = parse('lit', 'a', REGRAMMAR)
        answer = (['lit', 'a'], '')
        self.assertEqual(result, answer)

        result = parse('lit', 'a', REGRAMMAR)
        answer = (['lit', 'a'], '')
        self.assertEqual(result, answer)

    def test_group(self):
        result = parse('group', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('group', '(a)', REGRAMMAR)
        answer = (['group', '(', ['RE', ['alt',
                                         ['seq', ['RE2', ['RE1', ['lit', 'a']]]]]],
                   ')'], '')
        self.assertEqual(result, answer)

        result = parse('group', '(ab)', REGRAMMAR)
        answer = (['group', '(', ['RE', ['alt',
                                         ['seq', ['RE2', ['RE1', ['lit', 'a']]],
                                          ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]]],
                   ')'], '')
        self.assertEqual(result, answer)

    def test_oneof(self):
        result = parse('oneof', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('oneof', '[a]', REGRAMMAR)
        answer = (['oneof', '[', ['lits', ['lit', 'a']], ']'], '')
        self.assertEqual(result, answer)

        result = parse('oneof', '[ab]', REGRAMMAR)
        answer = (['oneof', '[', ['lits', ['lit', 'a'],
                                  ['lits', ['lit', 'b']]], ']'], '')
        self.assertEqual(result, answer)

    def test_opt(self):
        result = parse('opt', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('opt', 'a?', REGRAMMAR)
        answer = (['opt', ['RE1', ['lit', 'a']], '?'], '')
        self.assertEqual(result, answer)

    def test_plus(self):
        result = parse('plus', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('plus', 'a+', REGRAMMAR)
        answer = (['plus', ['RE1', ['lit', 'a']], '+'], '')
        self.assertEqual(result, answer)

    def test_star(self):
        result = parse('star', '', REGRAMMAR)
        answer = FAIL
        self.assertEqual(result, answer)

        result = parse('star', 'a*', REGRAMMAR)
        answer = (['star', ['RE1', ['lit', 'a']], '*'], '')
        self.assertEqual(result, answer)

    def test_seq(self):
        result = parse('seq', 'ab', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]],
                   ['seq', ['RE2', ['RE1', ['lit', 'b']]]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a.', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]],
                   ['seq', ['RE2', ['RE1', ['dot', '.']]]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a(ab)', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]],
                   ['seq',
                    ['RE2', ['RE1', ['group', '(', ['RE', ['alt',
                                                           ['seq', ['RE2', ['RE1', ['lit', 'a']]],
                                                            ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]]],
                                     ')']]]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a[ab]', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]],
                   ['seq', ['RE2', ['RE1',
                                    ['oneof', '[', ['lits', ['lit', 'a'],
                                                    ['lits', ['lit', 'b']]],
                                     ']']]]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a[ab]c', REGRAMMAR)
        answer = (['seq', ['RE2', ['RE1', ['lit', 'a']]],
                   ['seq', ['RE2', ['RE1', ['oneof',
                                            '[', ['lits', ['lit', 'a'],
                                                  ['lits', ['lit', 'b']]],
                                            ']']]],
                    ['seq', ['RE2', ['RE1', ['lit', 'c']]]]]], '')
        self.assertEqual(result, answer)

        result = parse('seq', 'a?b', REGRAMMAR)
        answer = (['seq', ['RE2', ['opt', ['RE1', ['lit', 'a']], '?']],
                   ['seq', ['RE2', ['RE1', ['lit', 'b']]]]], '')
        self.assertEqual(result, answer)

    def test_compound_modifiers(self):
        result = parse('seq', 'a?+', REGRAMMAR)
        answer = (['seq', ['RE2', ['optplus', ['RE1', ['lit', 'a']], '?+']]], '')
        self.assertEqual(result, answer)

    def test_group_modifier(self):
        result = parse('seq', '(a+)?', REGRAMMAR)
        answer = (['seq', ['RE2', ['opt', ['RE1', ['group', '(', ['RE', ['alt',
                                                                         ['seq', ['RE2', ['plus', ['RE1', ['lit', 'a']],
                                                                                          '+']]]]],
                                                   ')']], '?']]], '')
        self.assertEqual(result, answer)

    def test_alt(self):
        result = parse('alt', 'a|b', REGRAMMAR)
        answer = (['alt', ['seq', ['RE2', ['RE1', ['lit', 'a']]]],
                   '|', ['alt', ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]], '')
        self.assertEqual(result, answer)

        result = parse('alt', 'a|b*', REGRAMMAR)
        answer = (['alt', ['seq', ['RE2', ['RE1', ['lit', 'a']]]], '|',
                   ['alt', ['seq', ['RE2', ['star', ['RE1', ['lit', 'b']], '*']]]]], '')
        self.assertEqual(result, answer)

        result = parse('alt', '(a|b)', REGRAMMAR)
        answer = (['alt',
                   ['seq', ['RE2', ['RE1', ['group', '(', ['RE', ['alt',
                                                                  ['seq', ['RE2', ['RE1', ['lit', 'a']]]], '|',
                                                                  ['alt', ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]]],
                                            ')']]]]], '')
        self.assertEqual(result, answer)

    def test_re(self):
        result = parse('RE', 'a|b', REGRAMMAR)
        answer = (['RE', ['alt', ['seq', ['RE2', ['RE1', ['lit', 'a']]]],
                          '|', ['alt', ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]]], '')
        self.assertEqual(result, answer)

        result = parse('RE', 'a|b*', REGRAMMAR)
        answer = (['RE', ['alt', ['seq', ['RE2', ['RE1', ['lit', 'a']]]],
                          '|', ['alt', ['seq', ['RE2', ['star', ['RE1', ['lit', 'b']],
                                                        '*']]]]]], '')
        self.assertEqual(result, answer)

        result = parse('RE', '(a|b)', REGRAMMAR)
        answer = (['RE', ['alt', ['seq', ['RE2', ['RE1',
                                                  ['group', '(', ['RE',
                                                                  ['alt', ['seq', ['RE2', ['RE1', ['lit', 'a']]]], '|',
                                                                   ['alt', ['seq', ['RE2', ['RE1', ['lit', 'b']]]]]]],
                                                   ')']]]]]], '')
        self.assertEqual(result, answer)

    def test_parse_re(self):
        result = parse_re('a')
        answer = "lit('a')"
        print(result)
        self.assertEqual(result, answer)

        # result = parse_re('(a|b)?+')
        # answer = "plus(opt(alt(lit('a'), lit('b'))))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('(a|b)?*')
        # answer = "star(opt(alt(lit('a'), lit('b'))))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('a|b|c')
        # answer = "alt(lit('a'), alt(lit('b'), lit('c')))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('a+|b')
        # answer = "alt(plus(lit('a')), lit('b'))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('(a|b)+?')
        # answer = "opt(plus(alt(lit('a'), lit('b'))))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('[ab]')
        # answer = "oneof(seq(lit('a'), lit('b')))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('[ab]*')
        # answer = "star(oneof(seq(lit('a'), lit('b'))))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('ab+')
        # answer = "seq(lit('a'), plus(lit('b')))"
        # self.assertEqual(result, answer)
        #
        # result = parse_re('[ab]*abc')
        # answer = "seq(star(oneof(seq(lit('a'), lit('b')))), seq(lit('a'), seq(lit('b'), lit('c'))))"
        # self.assertEqual(result, answer)


if __name__ == '__main__':
    sys.argv.insert(1, '--verbose')
    unittest.main(argv=sys.argv)