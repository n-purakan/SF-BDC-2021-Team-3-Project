#Import necessary tools
import os
from datetime import datetime 

#In this program, summary data is generated for the entire data set. The text of all tweets created on each date in our study period are aggregated into separate text files. 
#Furthermore, the number of positive, negative and netural tweets for each day are tabulated and printed. 

# Opening file
file1 = open('/Users/eshanyepurakan/Downloads/BaselineTWEET/Cleaned+VADERedTweets.csv', 'r')
line1 = file1.readline().strip()
line2 = file1.readline().strip()

fields = line2.split(",") #For each tweet entry, split fields to collect data about that tweet
save_dt=fields[7] #Date and time of tweet creation FOR THE FIRST TWEET. Since this data is sorted by date, this is the first tweet created on
#the first day being considered. 
vclass=fields[6] #VADER classification 
ncount = 0 #Count of daily negative tweets
pcount = 0 #Count of daily positive tweets
neutcount=0 #Count of daily neutral tweets
words=fields[4] #Tweet text (cleaned)

#print("date,ncount,neutcount,pcount")

#Update statistics with information about first tweet entry 
if vclass == "POSITIVE":
    pcount += 1
else:
    if vclass == "NEGATIVE":
        ncount += 1
    else:
        neutcount += 1

#For each tweet in our data set
for line in file1:
    fields = line.strip().split(",") #extract metadata for this tweet
    this_dt=fields[7] #Date and time of tweet creation
    vclass=fields[6] #VADER classification for this tweet
    this_words=fields[4] #This tweet's text
    if this_dt != save_dt: #If this tweet was created on a 'new date', create a new 'daily words' summary file for this tweet 
        fname="W"+save_dt+"words.txt" 
        print(save_dt,",",ncount,",",neutcount,",",pcount,",",fname) 
        f = open(fname, "w") 
        f.write(words)
        f.close
        #Reset daily statistics 
        ncount = 0 
        pcount = 0
        neutcount = 0
        #update 'current' date 
        save_dt = this_dt
        #start fresh collection of daily words, starting with this first tweet 
        words=this_words
    else: # If this tweet was created on the date currently being analyzed
        words=words+this_words #Add text of this current tweet to the text aggregate of all tweets created on this day 
        #Update daily statistics
        if vclass == "POSITIVE":
            pcount += 1
        else:
            if vclass == "NEGATIVE":
                ncount += 1
            else:
                neutcount += 1

#Save the summary file for the last day. 
fname="W"+save_dt+"words.txt"
print(save_dt,",",ncount,",",neutcount,",",pcount,",",fname)
f = open(fname, "w")
f.write(words)
f.close
 
# Closing files
file1.close()
