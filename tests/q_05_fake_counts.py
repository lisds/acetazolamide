test = {
  'name': 'Question 05_fake_counts',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fake_stats'
          >>> 'fake_stats' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fake_stats'
          >>> # from its initial state (of ...)
          >>> fake_stats is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(fake_stats)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(fake_stats >= 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(fake_stats <= 19)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
