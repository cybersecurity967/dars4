def student_info(**infos):
    for key, value in infos.items():
        print(f"{key.capitalize()}: {value}")

student_info(ism="Aziz", kurs="2", shahar="Samarqand")