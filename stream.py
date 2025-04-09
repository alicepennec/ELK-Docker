from time import sleep

with open("temp/movies_elastic.json","r") as ifile:
    with open("logstash/movies1.json", "a") as ofile:
        n_lines = 200
        to_write = list()
        for line in ifile:
            to_write.append(line)
            if len(to_write) == n_lines:
                ofile.writelines(to_write)
                ofile.flush()
                to_write = list()
                sleep(120)