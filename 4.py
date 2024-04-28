marks={"Bill":78,"Tim":75,"Steve":80}
to_remove=["Tim","Jeff"]

for i in to_remove:
    if i in marks:
        marks.pop(i)
print(marks)
