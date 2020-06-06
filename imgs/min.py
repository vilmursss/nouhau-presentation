import htmlmin

with open("index.html", "r") as f:
	data = f.read()

with open("index_min.html", "w") as o:
	o.write(htmlmin.minify(data))
