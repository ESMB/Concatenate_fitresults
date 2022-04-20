#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:30:37 2021

@author: Mathew
"""

import os
import pandas as pd




# This will load any files containing this:

filename_contains="FitResults.txt"

# Folders to analyse:

pathList=[]





pathList.append(r"/Users/Mathew/Documents/Edinburgh Code/Concatenate_FitResults/Test/")



for path in pathList:
    
    j=0
    frame=0

    # Load the fits:
    for root, dirs, files in os.walk(path):
                for name in files:
                        if filename_contains in name:
                            # if ".txt" in name:
                                # if "_FitResults" not in name:
                                resultsname = name
                                print(resultsname)
    
                                fits_path=path+resultsname
    
                                data_df = pd.read_csv(fits_path,sep='\t')
                                
                                if j<1:
                                    data_all=data_df
                                else:
                                    # Increase frame number for each file
                                    data_df['Frame']=data_df['Frame']+frame
                                
                                    data_all=pd.concat([data_all,data_df])
                                    
                                    
                                # Frame counter
                                
                                frame=data_all['Frame'].max()
                                print(frame)
                                
                                j+=1
                                
    data_all.to_csv(path+'Contact.txt', sep='\t')
            
            