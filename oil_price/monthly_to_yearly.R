library(plyr)
df = read.csv("IMFPCP2014Jan.csv", header = TRUE)
df$yr <- strftime(input_df$Date, "%Y")
df$x <- df$Dubai.Crude.Oil.Price...US.per.barrel..IMFPCP2014Jan
results <- ddply(df, "yr", summarise, x = mean(x))
results <- rename(results, c("yr"="year", "x"="Dubai Crude Oil Price US per barrel IMFPCP2014Jan"))
write.csv(results,file = "IMFPCP2014Jan_yearly.csv")                  
