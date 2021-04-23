# SadaApp
Highest Profit
Michael Bermudez
4/23/21
Inputs: There are no inputs required
Outputs: 
  1) Prints out how many rows of data there is in the csv file.
  2) Prints an accurate number of valid entries after removing invalid profit entries
  3) Orders the data based on profit value and prints the top 20 highest profit
  4) Converts the updated file into a JSON file called data2.json
Code:Code reads in a csv file and prints out the numbers of rows of data there is in the csv file.
     It also removes rows from the read csv file with invalid Profit values and prints an accurate 
     number of valid entries. Code converts the updated file into a JSON file called data2.json and 
     lastly orders the data based on profit value and prints the top 20 highest profit

     Code uses a list comprehension inorder to remove invalid entries while iterating through the
     dictionary list of values. Also uses a sort function to order the data based on profit value and print
     the top 20 highest profit sorted from lowest to highest so order must be reversed
