Creator	"yFiles"
Version	"2.18"
graph
[
	hierarchic	1
	label	""
	directed	1
	node
	[
		id	0
		label	"out1"
		graphics
		[
			x	40.0
			y	156.0
			w	30.0
			h	30.0
			type	"triangle"
			fill	"#00FFFF"
			outline	"#000000"
		]
		LabelGraphics
		[
			text	"out1"
			fontSize	12
			fontName	"Dialog"
			anchor	"c"
		]
	]
	node
	[
		id	1
		label	"a"
		graphics
		[
			x	65.0
			y	15.0
			w	30.0
			h	30.0
			type	"triangle"
			fill	"#00FF00"
			outline	"#000000"
		]
		LabelGraphics
		[
			text	"a"
			fontSize	12
			fontName	"Dialog"
			anchor	"c"
		]
	]
	node
	[
		id	2
		label	"b"
		graphics
		[
			x	15.0
			y	15.0
			w	30.0
			h	30.0
			type	"triangle"
			fill	"#00FF00"
			outline	"#000000"
		]
		LabelGraphics
		[
			text	"b"
			fontSize	12
			fontName	"Dialog"
			anchor	"c"
		]
	]
	node
	[
		id	3
		label	"out1"
		graphics
		[
			x	40.0
			y	85.5
			w	30.0
			h	30.0
			type	"ellipse"
			fill	"#CCCCFF"
			outline	"#000000"
		]
		LabelGraphics
		[
			text	"out1"
			fontSize	12
			fontName	"Dialog"
			anchor	"c"
		]
	]
	edge
	[
		source	3
		target	1
		graphics
		[
			fill	"#000000"
			sourceArrow	"standard"
			Line
			[
				point
				[
					x	40.0
					y	85.5
				]
				point
				[
					x	40.0
					y	50.0
				]
				point
				[
					x	65.0
					y	50.0
				]
				point
				[
					x	65.0
					y	15.0
				]
			]
		]
	]
	edge
	[
		source	3
		target	2
		graphics
		[
			fill	"#000000"
			sourceArrow	"standard"
			Line
			[
				point
				[
					x	40.0
					y	85.5
				]
				point
				[
					x	40.0
					y	50.0
				]
				point
				[
					x	15.0
					y	50.0
				]
				point
				[
					x	15.0
					y	15.0
				]
			]
		]
	]
	edge
	[
		source	0
		target	3
		graphics
		[
			fill	"#000000"
			sourceArrow	"standard"
		]
	]
]
