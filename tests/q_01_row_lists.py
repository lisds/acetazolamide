test = {
  'name': 'Question row_lists',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'row_lists'
          >>> 'row_lists' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'row_lists'
          >>> # from its initial state (of ...)
          >>> row_lists is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(row_lists) == ams_counts.sum().sum()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> has_plac = [row for row in row_lists if row == ['Had AMS', 'Placebo']]
          >>> len(has_plac)
          17
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
