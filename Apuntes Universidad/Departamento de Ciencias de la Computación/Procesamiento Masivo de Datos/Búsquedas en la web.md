
Lo que hace un buscador genérico al hacer un *query* se divide en tres procesos principales: 

- **Crawling**: Parsear los enlaces de las páginas web 
- **Indexación**: Parsear las palabras claves 
- **Ranking**: Rankear las páginas 

# Crawling 

Lo que hace Google es, primero que nada, descargar la web: 

```c
crawl(list seedUrls)
	frontier_i = seedUrls
	while !frontier_i.isEmpty()
		new list frontier_i+1 
		for url : frontier_i 
			page = downloadPage(url)
			urlSeen.add(url)
			frontier_i+1.addAll(extractUrls(page).removeAll(urlsSeen))
			store(page)

i++ 
```

Sin embargo, descargar página por página es muy poco eficiente. Por lo mismo, es posible hacer *multi-threading*, donde se descargan las páginas mientras también verifica si la url ya está vista.