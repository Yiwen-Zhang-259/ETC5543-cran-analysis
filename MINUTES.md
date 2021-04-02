
# Minutes 

## Tue 9 Mar 2021

This week, Emi and I talked about things as followed:

1. First we go over the shiny app and Emi explains the "ngram" to me.
	
2. Then Emi tells me to change the layout of the shiny app and solve the data loading issue  (not need to load each time) to make it better.
	
3. Emi introduces the points of each direction : shiny, EDA…
	
4. Then we come to the Github repo, Emi introduces the project introduction in README file, and tell me to study the related literatures to do the summary of what others have done on this topic and figure out what I can do to extend the work.
	
5. Emi tells me to write something every week and push it to the Github repo to be on track.
	
6. Emi introduces the TODO file and the MINUTES file. The former is used to record the to do things each week and the latter is used to record the content of meeting each week, but after discussion, we think use issue to record the to do things is better. And we can post message or I can receive Emi's questions through that.
	
7. Emi teaches me how to generate the online book of this project in Github, and tells me that the output of this project can be one online book, one html or pdf book to be submitted and the shiny app.
	
8. Then, Emi explains the requirements of this ETC5543 course again. 
	
9. Next, Emi tells to define the related terms such as CRAN task view of this project and also introduce the function of this shiny app to make users understood.
	
10. Finally, we decided that every Tuesday is our regular meeting time.


## Tue 16 Mar 2021

This week, Emi and I talked about things as followed:

1. I first shared what I had done on shiny app. The specific things I have done include : 
   (1) I try to improve the layout of the app and try to figure out the way to speed up the data loading process.(but actually the way I used is wrong
   (2) I read all the related literatures and write summaries on this, so I share the interesting I learned from these packages
   
2. Emi told me the method to make the data loading faster by download a part of the whole data into the local computer first then everytime users need to use the data, they don't have to read it from the website every time. I will try to complete this this week.

3. Emi told me that I should make the interactive table more complicated by linking package name to its downlod log plot.

4. Emi told me dig deeper into the three most interesting packages `packageRank`, `adjustedcranlogs` and `pkgsearch` to figure out the specific method (i.e. the specific mathematical method) they used to achieve their goals. Also thinking about how could I do this? Is there some better way? Or could I extend the exist functions?

5. Emi helped me with the gitbook issue to make it possible for me to generate the remote site book on github.

6. Emi also reminded me that remember to commit regularly and do spend enough time on this project.


## Tue 23 Mar 2021

This week, Emi and I talked about things as followed:

1. Emi correct my misunderstanding of the related literature (for what are these packages used for).

2. Emi told me that we should focus on our title : 'The evolution of R'.
DETAILS: R started 1993, and `tidverse` is very popular from its start. The R community is quite different to the initial one, so look into how things has   changed is a good idea. And we should try to figure out that how the evolution happend. As a part of that, I can take on the package ranking. In other words, how has the package ranking changed over time? 

Some packages's downloads may increase linearly, others may not. By looking into the insights of these may help find something.

Another direction is analysing how has the statistics changed over time for many R package developers are statisticians.

3. Emi sends me a paper on analysis for Github repo popularity as an example. So in my case, maybe I can looking on what areas are people interested in.
   Emi also suggests me refer to this paper to think about my analysis. And Emi said I can classify packages by doing clustering analysis. i.e. the classify the packages by their speed of growth, such as high growth and slow growth.
   
   Emi suggests me just go though top 15 packages for it's hard to do with all.
   
4. But there is a problem that the data available in CRAN is just begin from 2012, so there are not enough for us. So maybe I can't see the popularity, but I can see what packages exsit. That means I can figure out what sort of things people did before 2012, and what they have done after 2012.

5. So I can figure out what are top 15 packages from the available date from 2012 and have a look at how this changes every day.

6. Emi thinks that popular packages are probably larges rows around all of `tidyverse` packages, for they are dependent packages and people just downloaded these with purpose for downloading the `tidyverse`.

7. Emi advices me to create a model to describe what happende across time rather than doing predictions.
   

## Tue 30 Mar 2021

This week, Emi Hien, and I talked about things as followed:

1. I report what I did last week.

2. Emi told me that I should extract the number of updates of packages. And plot to compare the downloads against the number of updates of certain package.

3. Emi told me to look at the type of the top 15 packages.

4. 
