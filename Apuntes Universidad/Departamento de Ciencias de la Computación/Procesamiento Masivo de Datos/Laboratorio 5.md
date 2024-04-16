
Today we’re going to analyse TV shows to get their average episode rating and a list of their best-rated episodes. We will use data from IMDb (the same as Lab 4), which look like:

The columns are: (1) the number of votes, (2) the average vote, (3) the series name, (4) the series year, (5) the type,
(6) the name of the episode. Where column (6) is null for a TV series, the voting information is the overall for the
series (on IMDb, one can vote on the series page or on an individual episode). The data are on the HDFS storage of
the cluster: hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings.tsv. We want to compute output tuples of the form:

TheWire#2002 -30- (#5.10)|Middle Ground (#3.11) 9.6 8.583

Where the columns are: (1) a key for the series (name#year), (2) a list of episodes tied for best rating using ‘|’
as a delimiter, (3) the best rating of an episode (and thus the ratings of episodes in (2)), (4) the average rating of all
episodes (excluding the series value, e.g., the first line in the input above)

We will use Spark for processing. For testing, hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings-two.tsv is
a small example file with two series and an irrelevant movie you should filter; one of the series is The Wire (2002),whose
results should correspond to the those indicated above (modulo some minor rounding differences). Note that the actual
output given by Spark will use commas and brackets rather than tabs, which is fine: the syntax of the lines is not
important, but rather we care about the content of each line. Also be aware that Spark will often include
multiple output files of the type part-NNNNN in the output folder; all of these form part of the output. (You
can use “part-*” in combination with cat to concatenate the different output parts, where * acts as a wildcard.)
There are multiple options with which to run Spark, including Java, Scala, Python and R. Of these options, both
Java and Scala can be considered “native” as – like Spark – they run in the Java Virtual Machine (JVM). The server
we will use can run Java, Scala and Python. You can submit the work in Java, Scala or Python.

Now to the main task: your goal is to use Spark Core to output for each series, (1) the average episode rating,
(2) the best episode rating, and (3) the names of episodes with the best rating, as per the example in the
introduction. You need to copy the AverageSeriesRating file in the language of your choice to a new file called
InfoSeriesRating and start extending it to look for info on the best episodes. In so doing, you should follow
the example of AverageSeriesRating, reading the input from HDFS and writing the output to HDFS. You
should test this on the small example provided before running it on the full file. In the case of Python and Scala,
we highly recommend developing the new script line-by-line in the respective shell, revising the output as you
proceed over the example. You should also ensure to cache any RDDs you use more than once. Please see the
example output in the introduction for The Wire#2002 for the task you need to build; again note that is not
necessary to have the exact syntax shown for each line, just the correct information on each line.
 Once your code is ready and working on the small file, you should run it on the full ratings data found in
hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings.tsv and revise the results.

## Java snippets 

This is an optional guide to help you code your solution in Java. You should start by copying the class called AverageSeriesRating.java to the same package with the name InfoSeriesRating.java. The code given to you in
AverageSeriesRating.java computes the average rating of episodes in a series, which you should extend with the
information about the names of the best-rated episodes and their rating. You can extend the given code with the
following snippets to complete the lab. Snippets may be out of order but are sufficient to complete the lab. Note that:

- You will need to change the names of rdd1, rdd2 and rdd3 (the new names might be different every time;
some RDD names might already appear in the code of AverageSeriesRating.java).
- You may need to modify parts of the code already given to you in AverageSeriesRating.java.
- You may also need to change the name of the RDD that you store to HDFS towards the end of the code.
- Where you see a question mark “?”, this means that you need to fill the slot with some code.

**Cache**: This caches the RDD rdd2 as rdd1 in order to use it multiple times without recomputing it from scratch
each time. You should henceforth refer to rdd1 rather than rdd2 to avoid the re-computation. Note that this might require modifying code already given in AverageSeriesRating.java.

```Java 
JavaRDD<Tuple3><String, String, Double>> rdd1 = rdd2.cache();
```

**Map-to-pair**: This creates a `PairRDD rdd1` from `rdd2` 

```Java 
JavaPairRDD<String,Tuple2<String,Double>> rdd1 = rdd2.mapToPair(

?

);
```

**Reduce-by-key**: This creates a new `RDD rdd1` resulting from a reduce-by-key on `rdd2`-  

```Java 
JavaPairRDD<String,Tuple2<String,Double>> rdd1 = rdd2.reducebyKey(

?

);