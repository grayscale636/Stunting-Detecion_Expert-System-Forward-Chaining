import streamlit as st

st.write("""
### STUNTING DETECTION
""")

umur = st.number_input("Masukkan Umur (dalam bulan): ", step=1)
jk = st.text_input("Masukkan Jenis Kelamin (L/P): ")
bb = st.number_input("Masukkan Berat Badan (dalam kg): ")
tb = st.number_input("Masukkan Tinggi Badan (dalam cm): ")

pred = st.button("Prediksi")

if pred:
    if umur == 1:
        if jk == 'p' or jk == 'P': 
            if bb < 3.2 and tb < 49.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 3.4 and tb < 50:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 2:
        if jk == 'p' or jk == 'P': 
            if bb < 3.9 and tb < 53.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 4.3 and tb < 54.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 3:
        if jk == 'p' or jk == 'P': 
            if bb < 4.5 and tb < 55.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 5.0 and tb < 57.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 4:
        if jk == 'p' or jk == 'P': 
            if bb < 5.0 and tb < 57.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 5.6 and tb < 59.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 5:
        if jk == 'p' or jk == 'P': 
            if bb < 5.4 and tb < 59.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 6.0 and tb < 61.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 6:
        if jk == 'p' or jk == 'P': 
            if bb < 5.7 and tb < 61.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 6.4 and tb < 63.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 7:
        if jk == 'p' or jk == 'P': 
            if bb < 6.0 and tb < 62.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 6.7 and tb < 64.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 8:
        if jk == 'p' or jk == 'P': 
            if bb < 6.3 and tb < 64.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 6.9 and tb < 66.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 9:
        if jk == 'p' or jk == 'P': 
            if bb < 6.5 and tb < 65.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.1 and tb < 67.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 10:
        if jk == 'p' or jk == 'P': 
            if bb < 6.7 and tb < 66.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.1 and tb < 68.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 11:
        if jk == 'p' or jk == 'P': 
            if bb < 6.9 and tb < 67.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.6 and tb < 69.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 12:
        if jk == 'p' or jk == 'P': 
            if bb < 68.9 and tb < 7.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.7 and tb < 71.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 13:
        if jk == 'p' or jk == 'P': 
            if bb < 7.2 and tb < 70.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.9 and tb < 72.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 14:
        if jk == 'p' or jk == 'P': 
            if bb < 7.4 and tb < 71.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 7.9 and tb < 72.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 15:
        if jk == 'p' or jk == 'P': 
            if bb < 7.6 and tb < 72.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 8.3 and tb < 74.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 16:
        if jk == 'p' or jk == 'P': 
            if bb < 7.7 and tb < 73.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 8.4 and tb < 75.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 17:
        if jk == 'p' or jk == 'P': 
            if bb < 7.9 and tb < 74.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 8.6 and tb < 76.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 18:
        if jk == 'p' or jk == 'P': 
            if bb < 8.1 and tb < 74.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 8.8 and tb < 76.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 20:
        if jk == 'p' or jk == 'P': 
            if bb < 8.4 and tb < 7.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.1 and tb < 78.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 21:
        if jk == 'p' or jk == 'P': 
            if bb < 8.6 and tb < 77.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.2 and tb < 79.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 22:
        if jk == 'p' or jk == 'P': 
            if bb < 8.7 and tb < 78.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.4 and tb < 80.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 23:
        if jk == 'p' or jk == 'P': 
            if bb < 8.9 and tb < 79.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.5 and tb < 81.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 24:
        if jk == 'p' or jk == 'P': 
            if bb < 9.0 and tb < 80.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.7 and tb < 81.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 25:
        if jk == 'p' or jk == 'P': 
            if bb < 9.2 and tb < 8.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 9.8 and tb < 81.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 26:
        if jk == 'p' or jk == 'P': 
            if bb < 9.4 and tb < 80.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.0 and tb < 82.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 27:
        if jk == 'p' or jk == 'P': 
            if bb < 9.5 and tb < 81.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.2 and tb < 83.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 28:
        if jk == 'p' or jk == 'P': 
            if bb < 9.7 and tb < 82.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.2 and tb < 83.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 29:
        if jk == 'p' or jk == 'P': 
            if bb < 9.8 and tb < 82.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.4 and tb < 84.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 30:
        if jk == 'p' or jk == 'P': 
            if bb < 10.0 and tb < 83.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.5 and tb < 85.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 31:
        if jk == 'p' or jk == 'P': 
            if bb < 10.1 and tb < 84.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.7 and tb < 85.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 32:
        if jk == 'p' or jk == 'P': 
            if bb < 10.3 and tb < 84.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.8 and tb < 86.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 33:
        if jk == 'p' or jk == 'P': 
            if bb < 10.4 and tb < 85.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 10.9 and tb < 86.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 34:
        if jk == 'p' or jk == 'P': 
            if bb < 10.5 and tb < 86.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.0 and tb < 87.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 35:
        if jk == 'p' or jk == 'P': 
            if bb < 10.7 and tb < 86.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.2 and tb < 88.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 36:
        if jk == 'p' or jk == 'P': 
            if bb < 10.8 and tb < 87.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.4 and tb < 88.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 37:
        if jk == 'p' or jk == 'P': 
            if bb < 10.9 and tb < 88.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.4 and tb < 89.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 38:
        if jk == 'p' or jk == 'P': 
            if bb < 11.1 and tb < 88.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.5 and tb < 89.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 39:
        if jk == 'p' or jk == 'P': 
            if bb < 11.2 and tb < 89.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.6 and tb < 90.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 40:
        if jk == 'p' or jk == 'P': 
            if bb < 11.3 and tb < 89.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.8 and tb < 90.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 41:
        if jk == 'p' or jk == 'P': 
            if bb < 11.5 and tb < 90.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 11.9 and tb < 91.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 42:
        if jk == 'p' or jk == 'P': 
            if bb < 11.6 and tb < 90.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.0 and tb < 91.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 43:
        if jk == 'p' or jk == 'P': 
            if bb < 11.7 and tb < 91.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.1 and tb < 92.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 44:
        if jk == 'p' or jk == 'P': 
            if bb < 11.8 and tb < 92.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.2 and tb < 93.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 45:
        if jk == 'p' or jk == 'P': 
            if bb < 12.0 and tb < 92.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.5 and tb < 93.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 46:
        if jk == 'p' or jk == 'P': 
            if bb < 93.1 and tb < 12.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.5 and tb < 94.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 47:
        if jk == 'p' or jk == 'P': 
            if bb < 12.2 and tb < 93.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.6 and tb < 94.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 48:
        if jk == 'p' or jk == 'P': 
            if bb < 12.3 and tb < 94.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.7 and tb < 94.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 49:
        if jk == 'p' or jk == 'P': 
            if bb < 12.4 and tb < 94.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.8 and tb < 95.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()


    elif umur == 50:
        if jk == 'p' or jk == 'P': 
            if bb < 12.6 and tb < 95.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 12.9 and tb < 95.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 51:
        if jk == 'p' or jk == 'P': 
            if bb < 12.7 and tb < 95.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.1 and tb < 96.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 52:
        if jk == 'p' or jk == 'P': 
            if bb < 12.8 and tb < 96.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.2 and tb < 96.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 53:
        if jk == 'p' or jk == 'P': 
            if bb < 12.9 and tb < 96.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.3 and tb < 97.4:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 54:
        if jk == 'p' or jk == 'P': 
            if bb < 13.0 and tb < 97.6:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.4 and tb < 97.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 55:
        if jk == 'p' or jk == 'P': 
            if bb < 13.2 and tb < 96.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.5 and tb < 98.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 56:
        if jk == 'p' or jk == 'P': 
            if bb < 13.3 and tb < 98.1:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.6 and tb < 98.8:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 57:
        if jk == 'p' or jk == 'P': 
            if bb < 13.4 and tb < 98.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.7 and tb < 99.3:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 58:
        if jk == 'p' or jk == 'P': 
            if bb < 13.5 and tb < 99.0:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 13.8 and tb < 99.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 59:
        if jk == 'p' or jk == 'P': 
            if bb < 13.6 and tb < 99.5:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 14.0 and tb < 100.2:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()

    elif umur == 60:
        if jk == 'p' or jk == 'P': 
            if bb < 13.7 and tb < 99.9:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        elif jk == 'l' or jk == 'L':
            if bb < 14.1 and tb < 100.7:
                st.success("Hasil Prediksi : Stunting")
                st.balloons()
            else:
                st.success("Hasil Prediksi : Tidak Stunting")
                st.balloons()
        else:
            st.success("Masukkan Jenis Kelamin Yang Valid")
            st.balloons()
    else:
        st.success("Sudah Bukan Usia Balita")
        st.balloons()