from textblob import TextBlob
statement = TextBlob ('Campk12 is a good compny and alays valule ttheir employeees')
statement = statement.correct()
print(statement)