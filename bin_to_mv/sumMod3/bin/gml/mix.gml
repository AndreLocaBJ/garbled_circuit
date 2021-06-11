graph [

    node [ id     5 label "f1"
        graphics [ type "triangle" fill "#00FFFF" ]
    ]
    node [ id     6 label "f2"
        graphics [ type "triangle" fill "#00FFFF" ]
    ]

    node [ id     1 label "x1"
        graphics [ type "triangle" fill "#00FF00" ]
    ]
    node [ id     2 label "x2"
        graphics [ type "triangle" fill "#00FF00" ]
    ]
    node [ id     3 label "y1"
        graphics [ type "triangle" fill "#00FF00" ]
    ]
    node [ id     4 label "y2"
        graphics [ type "triangle" fill "#00FF00" ]
    ]


    node [ id    46 label "f1"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]
    node [ id    74 label "n_74"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]
    node [ id    81 label "n_81"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]
    node [ id    84 label "f2"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]

    edge [ source    46   target     1
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    46   target     2
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    46   target     3
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    46   target     4
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    46   target    74
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    46   target    81
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    74   target     1
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    74   target     2
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    81   target     3
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    81   target     4
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target     1
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target     2
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target     3
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target     4
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target    74
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source    84   target    81
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     5   target    46
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     6   target    84
        graphics [ type "line" arrow "first" ]
    ]
]

