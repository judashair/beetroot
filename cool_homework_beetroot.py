files = ["april_dashboard.xlsx", "may_dashboard.xlsx", "june_dashboard.xlsx",
         "july_dashboard.xlsx", "october_dashboard.xlsx", "Pro football theory 353-pages.pdf",
         "Clean Code 250-pages.pdf", "War&Peace 150-pages.pdf", "IKEA Instruction 35-pages.pdf",
         "october_dashboard.pptx", "july_dashboard.pptx", "(thriller) The Gray Man (2022).mp4",
         "(thriller) Level 16 (2018).mp4", "(thriller) Synchronic (2019).mp4",
         "(comedy) The Philadelphia Story (1940).mp4", "(comedy) Harold and Maude (1971).mp4",
         "(comedy) Booksmart (2019).mp4"]

for file in files:
    print(file)

number_of_files = len(files)
print(f"\nNumber of files in folder \"Downloads\" is {number_of_files}.\n")

file_extensions = []
for file in files:
    file_extension = file.split(".")[-1]
    if file_extension not in file_extensions:
        file_extensions.append(file_extension)
print(file_extensions, "\n")

excel_files = []
powerpoint_files = []
book_files = []
video_files = []

for file in files:
    if file.endswith("xlsx"):
        excel_files.append(file)
    elif file.endswith("pptx"):
        powerpoint_files.append(file)
    elif file.endswith("pdf"):
        book_files.append(file)
    elif file.endswith("mp4"):
        video_files.append(file)

print("Excel files:", excel_files, end="\n\n")
print("PowerPoint files:", powerpoint_files, end="\n\n")
print("Book files:", book_files, end="\n\n")
print("Video files:", video_files, end="\n\n")

Q1 = ["January", "February", "March"]
Q2 = ["April", "May", "June"]
Q3 = ["July", "August", "September"]
Q4 = ["October", "November", "December"]

excel_files_for_boss = []
for excel_file in excel_files:
    month, _ = excel_file.split("_")
    if month.title() in Q2:
        excel_files_for_boss.append(excel_file)
print(excel_files_for_boss, "\n")

excel_files_for_boss = []
for excel_file in excel_files:
    excel_file_name, _ = excel_file.split(".")

    for powerpoint_file in powerpoint_files:
        powerpoint_file_name, _ = powerpoint_file.split(".")

        if excel_file_name == powerpoint_file_name:
            excel_files_for_boss.append(excel_file)

print(excel_files_for_boss, "\n")

read_list = []
for book_file in book_files:
    book_file_name = book_file.split(" ")[-1]
    book_file_number, _ = book_file_name.split("-")
    if 120 < int(book_file_number) < 300:
        read_list.append(book_file)

print(read_list, "\n")

video_to_watch_for_fun = []
new_video_to_watch = []
maybe_later = []

for video_file in video_files:
    splited_text = video_file.split()
    genre, year = splited_text[0], splited_text[-1]
    genre = genre[genre.find("(")+1:genre.find(")")]
    year = year[year.find("(")+1:year.find(")")]
    year = int(year)

    if ((genre == "comedy") and (year < 2000)) and video_file not in video_to_watch_for_fun:
    video_to_watch_for_fun.append(video_file)
elif ((genre == "comedy") or (genre == "thriller") and (year >= 2019)):
    new_video_to_watch.append(video_file)
else:
    maybe_later.append(video_file)

video_to_watch_for_fun = ",".join(video_to_watch_for_fun)
new_video_to_watch = ",".join(new_video_to_watch)
maybe_later = ",".join(maybe_later)

print("I want to watch it for fun:", video_to_watch_for_fun, end="\n\n")
print("I want to watch new video:", new_video_to_watch, end="\n\n")
print("Nah, I might watch it later:", maybe_later, end="\n\n")







