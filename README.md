# ETC5543 Research Project

This repo contains the research project as part of ETC5543 for **Yiwen Zhang**.


# Goals

1. Extend existing R Shiny app (found [here](https://github.com/emitanaka/shinyctv)). The app contains interactive analysis of CRAN download logs and textual analysis of the title and descriptions of packages by the CRAN Task View.
1. Exploratory data analysis of CRAN download logs. Some obvious trends include a drop in download counts over the weekend and a spike when there is an update in the CRAN. Some questions to ask are:
  - Are older packages more downloaded? Does this mean that even if a better R package comes along then the
  - How does an update to R affect download?
  - The download counts are inflated due to bots and mirror downloads. How to adjust the download counts?
1. Find related literatures. Some to consider are:
  - [`rtrends`](https://cran.r-project.org/web/packages/rtrends/rtrends.pdf) - although it's not clear to me this is doing anything particularly striking.
  - [`adjustedcranlogs`](https://github.com/tylermorganwall/adjustedcranlogs). It looks like sub-samples some CRAN packages and takes a certain quantile to subtract the download count. 
  = [`packageRank`](https://github.com/lindbrook/packageRank). Also see [intro post](https://blog.r-hub.io/2020/05/11/packagerank-intro/) which is really well written!
  - [`cranlogs`](https://github.com/r-hub/cranlogs) - to download the summary download data. 
  - [`cran.stats`](https://github.com/arunsrinivasan/cran.stats)
  - [`dlstats`](https://github.com/GuangchuangYu/dlstats)
  - [`pkgsearch`](https://github.com/r-hub/pkgsearch/)
  - [`Visualize.CRAN.Downloads`](https://cran.r-project.org/web/packages/Visualize.CRAN.Downloads/vignettes/Visualize.CRAN.Downloads.html)
  
# Peripheral

- [cranlogs.app](https://github.com/r-hub/cranlogs.app)
- [Bioconductor](https://bioconductor.org/packages/stats/)
  
# Data sources

- CRAN package download logs http://cran-logs.rstudio.com/