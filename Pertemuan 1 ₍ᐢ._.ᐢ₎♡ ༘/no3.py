niu = int(input("Masukan NIU: "))
nilai_tugas = int(input("Masukan Nilai Tugas: "))
nilai_laporan = int(input("Masukan Nilai: "))

jml_nilai = nilai_tugas + nilai_laporan
rata_rata = jml_nilai / 2

if rata_rata < 40 :
    print("Nilai: K")
else:
    nilai_ujian = int(input("Masukan Nilai Ujian: "))
    bobot_tugas = nilai_tugas*0.25
    bobot_laporan = nilai_laporan*0.25
    bobot_ujian = nilai_ujian*0.5
    nilai_final = bobot_laporan+bobot_tugas+bobot_ujian
    if 80 <= nilai_final <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_final < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_final < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_final < 60:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"
    print("Nilai Huruf: ", nilai_huruf)