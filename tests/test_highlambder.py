from highlambder import L as λ

def test_all():

    assert λ(10) == 10

    assert (λ + 5)(10) == 15
    assert (5 + λ)(10) == 15
    assert (λ + 5 + 3)(10) == 18
    assert (5 + λ + 3)(10) == 18
    assert (5 + 3 + λ)(10) == 18

    assert (λ - 5)(10) == 5
    assert (5 - λ)(10) == -5
    assert (λ - 5 - 3)(10) == 2
    assert (5 - λ - 3)(10) == -8
    assert (5 - 3 - λ)(10) == -8

    assert (λ * 5)(10) == 50
    assert (5 * λ)(10) == 50
    assert (λ * 5 * 3)(10) == 150
    assert (5 * λ * 3)(10) == 150
    assert (5 * 3 * λ)(10) == 150

    assert (3 + λ * 2)(10) == 23
    assert (3 * λ + 2)(10) == 32
    assert (5 + 3 * λ + 2)(10) == 37

    assert (λ / 10)(20) == 2
    assert (10 / λ)(5) == 2
    assert (40 / λ / 5)(2) == 4

    assert (1 + 3 * λ / 2 - 5)(10) == 11

    assert (2 + λ.real)(5) == 7

    assert λ[1]([1, 2, 3]) == 2
    assert (10 * λ[1])([1, 2, 3]) == 20

    assert ((λ)(20 > 10)) is True
    assert ((λ)(20 < 10)) is False

    assert ((λ(20)) > λ(10)) is True
    assert ((λ(20)) < λ(10)) is False

    assert (-1 + λ * 5 / λ + 1)(13) == 5
    assert (λ * 2 + λ * 4 + λ)(10) == 70
    assert (λ['A'] + λ['B'])({'A': 3, 'B': 4}) == 7

    assert (λ + λ)(2) == 4

    assert ('ciao ' + λ)('Mario') == 'ciao Mario'

    if False:

        # Work in progress

        import pandas as pd
        import numpy as np

        df = pd.DataFrame({
            'A': [1, 1, 2, 2],
            'B': [5, 6, 7, 8],
            'C': ['banana', 'apple', 'kiwi', 'orange'],
        })

        assert pd.DataFrame.equals(
            df.assign(D=λ.A + 20),
            df.assign(D=lambda d: d.A + 20)
        )

        assert pd.DataFrame.equals(
            df.groupby('A')['B'].agg(λ.max),
            df.groupby('A')['B'].agg(lambda s: s.max())
        )

        assert pd.DataFrame.equals(
            df.assign(D=lambda d: d['C'].str.len() * 2),
            df.assign(D=λ['C'].str.len * 2)
        )

        assert (λ + 2)(np.int64(2)) == 4

        assert (λ.max - λ.min)(np.array([3, 4, 5, 6, 7, 8])) == 5

        assert pd.DataFrame.equals(
            df.apply(λ['A'] + λ['B'], axis=1),
            df.apply(lambda r: r['A'] + r['B'], axis=1)
        )

        temp = {
            'A': np.array([3, 4, 5, 6, 7, 8]),
            'B': np.array([3, 4, 5, 6, 7, 8]),
        }
        print(temp)
        assert np.array_equal(
            (λ['A'] + λ['B'])(temp),
            (lambda a: a['A'] + a['B'])(temp)
        )
        del temp

        assert pd.DataFrame.equals(
            df.assign(D=λ['A'] + λ['B']),
            df.assign(D=lambda d: d['A'] + d['B'])
        )

        #######################

        # TODO:
        # assert (λ1 + λ2)(3, 4) == 7
