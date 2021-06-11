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


    node [ id     7 label "f1"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]
    node [ id     8 label "f2"
        graphics [ type "ellipse" fill "#CCCCFF" ]
    ]

    edge [ source     7   target     1
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     7   target     2
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     7   target     3
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     7   target     4
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     8   target     1
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     8   target     2
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     8   target     3
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     8   target     4
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     5   target     7
        graphics [ type "line" arrow "first" ]
    ]
    edge [ source     6   target     8
        graphics [ type "line" arrow "first" ]
    ]
]

