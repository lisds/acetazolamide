test = {
  'name': 'Question people',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'people'
          >>> 'people' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'people'
          >>> # from its initial state (of ...)
          >>> people is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(people) == ams_counts.sum().sum()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(people) == ['AMS', 'Drug']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pd.crosstab(people['AMS'], people['Drug']).equals(ams_counts)
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
