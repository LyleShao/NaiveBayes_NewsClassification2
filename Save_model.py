from count_freqency import CountFrequency, adjust_frequency
import time
from Save_Load import save


filename01 = 'alt_atheism'
filename02 = 'comp_graphics'
filename03 = 'comp_os_ms_windows-misc'
filename04 = 'comp_sys_ibm_pc_hardware'
filename05 = 'comp_sys_mac_hardware'
filename06 = 'comp_windows_x'
filename07 = 'misc_forsale'
filename08 = 'rec_autos'
filename09 = 'rec_motorcycles'
filename10 = 'rec_sport_baseball'
filename11 = 'rec_sport_hockey'
filename12 = 'sci_crypt'
filename13 = 'sci_electronics'
filename14 = 'sci_med'
filename15 = 'sci_space'
filename16 = 'soc_religion_christian'
filename17 = 'talk_politics_guns'
filename18 = 'talk_politics_mideast'
filename19 = 'talk_politics_misc'
filename20 = 'talk_religion_misc'


total_start = time.time()

m1 = CountFrequency('data_train/alt.atheism')
print(f"Training alt.atheism Model")
start = time.time()
m1.catch_data()
m1.break_data()
f1 = m1.frequency_counter()
f1 = adjust_frequency(f1)
end = time.time()
used_time = end - start
print(f"alt.atheism Model now finished, time use {used_time} seconds")
save(f1, filename01)

m2 = CountFrequency('data_train/comp.graphics')
print(f"Training comp.graphics Model")
start = time.time()
m2.catch_data()
m2.break_data()
f2 = m2.frequency_counter()
f2 = adjust_frequency(f2)
end = time.time()
used_time = end - start
print(f"comp.graphics Model now finished, time use {used_time} seconds")
save(f2, filename02)

m3 = CountFrequency('data_train/comp.os.ms-windows.misc')
print(f"Training comp.os.ms-windows.misc Model")
start = time.time()
m3.catch_data()
m3.break_data()
f3 = m3.frequency_counter()
f3 = adjust_frequency(f3)
end = time.time()
used_time = end - start
print(f"comp.os.ms-windows.misc Model now finished, time use {used_time} seconds")
save(f3, filename03)

m4 = CountFrequency('data_train/comp.sys.ibm.pc.hardware')
print(f"Training comp.sys.ibm.pc.hardware Model")
start = time.time()
m4.catch_data()
m4.break_data()
f4 = m4.frequency_counter()
f4 = adjust_frequency(f4)
end = time.time()
used_time = end - start
print(f"comp.sys.ibm.pc.hardware Model now finished, time use {used_time} seconds")
save(f4, filename04)

m5 = CountFrequency('data_train/comp.sys.mac.hardware')
print(f"Training comp.sys.mac.hardware Model")
start = time.time()
m5.catch_data()
m5.break_data()
f5 = m5.frequency_counter()
f5 = adjust_frequency(f5)
end = time.time()
used_time = end - start
print(f"comp.sys.mac.hardware Model now finished, time use {used_time} seconds")
save(f5, filename05)

m6 = CountFrequency('data_train/comp.windows.x')
print(f"Training comp.windows.x Model")
start = time.time()
m6.catch_data()
m6.break_data()
f6 = m6.frequency_counter()
f6 = adjust_frequency(f6)
end = time.time()
used_time = end - start
print(f"comp.windows.x Model now finished, time use {used_time} seconds")
save(f6, filename06)

m7 = CountFrequency('data_train/misc.forsale')
print(f"Training misc.forsale Model")
start = time.time()
m7.catch_data()
m7.break_data()
f7 = m7.frequency_counter()
f7 = adjust_frequency(f7)
end = time.time()
used_time = end - start
print(f"misc.forsale Model now finished, time use {used_time} seconds")
save(f7, filename07)

m8 = CountFrequency('data_train/rec.autos')
print(f"Training rec.autos Model")
start = time.time()
m8.catch_data()
m8.break_data()
f8 = m8.frequency_counter()
f8 = adjust_frequency(f8)
end = time.time()
used_time = end - start
print(f"rec.autos Model now finished, time use {used_time} seconds")
save(f8, filename08)

m9 = CountFrequency('data_train/rec.motorcycles')
print(f"Training rec.motorcycles Model")
start = time.time()
m9.catch_data()
m9.break_data()
f9 = m9.frequency_counter()
f9 = adjust_frequency(f9)
end = time.time()
used_time = end - start
print(f"rec.motorcycles Model now finished, time use {used_time} seconds")
save(f9, filename09)

m10 = CountFrequency('data_train/rec.sport.baseball')
print(f"Training rec.sport.baseball Model")
start = time.time()
m10.catch_data()
m10.break_data()
f10 = m10.frequency_counter()
f10 = adjust_frequency(f10)
end = time.time()
used_time = end - start
print(f"rec.sport.baseball Model now finished, time use {used_time} seconds")
save(f10, filename10)

m11 = CountFrequency('data_train/rec.sport.hockey')
print(f"Training rec.sport.hockey Model")
start = time.time()
m11.catch_data()
m11.break_data()
f11 = m11.frequency_counter()
f11 = adjust_frequency(f11)
end = time.time()
used_time = end - start
print(f"rec.sport.hockey Model now finished, time use {used_time} seconds")
save(f11, filename11)

m12 = CountFrequency('data_train/sci.crypt')
print(f"Training sci.crypt Model")
start = time.time()
m12.catch_data()
m12.break_data()
f12 = m12.frequency_counter()
f12 = adjust_frequency(f12)
end = time.time()
used_time = end - start
print(f"sci.crypt Model now finished, time use {used_time} seconds")
save(f12, filename12)

m13 = CountFrequency('data_train/sci.electronics')
print(f"Training sci.electronics Model")
start = time.time()
m13.catch_data()
m13.break_data()
f13 = m13.frequency_counter()
f13 = adjust_frequency(f13)
end = time.time()
used_time = end - start
print(f"sci.electronics Model now finished, time use {used_time} seconds")
save(f13, filename13)

m14 = CountFrequency('data_train/sci.med')
print(f"Training sci.med Model")
start = time.time()
m14.catch_data()
m14.break_data()
f14 = m14.frequency_counter()
f14 = adjust_frequency(f14)
end = time.time()
used_time = end - start
print(f"sci.med Model now finished, time use {used_time} seconds")
save(f14, filename14)

m15 = CountFrequency('data_train/sci.space')
print(f"Training sci.space Model")
start = time.time()
m15.catch_data()
m15.break_data()
f15 = m15.frequency_counter()
f15 = adjust_frequency(f15)
end = time.time()
used_time = end - start
print(f"sci.space Model now finished, time use {used_time} seconds")
save(f15, filename15)

m16 = CountFrequency('data_train/soc.religion.christian')
print(f"Training soc.religion.christian Model")
start = time.time()
m16.catch_data()
m16.break_data()
f16 = m16.frequency_counter()
f16 = adjust_frequency(f16)
end = time.time()
used_time = end - start
print(f"soc.religion.christian Model now finished, time use {used_time} seconds")
save(f16, filename16)

m17 = CountFrequency('data_train/talk.politics.guns')
print(f"Training talk.politics.guns Model")
start = time.time()
m17.catch_data()
m17.break_data()
f17 = m17.frequency_counter()
f17 = adjust_frequency(f17)
end = time.time()
used_time = end - start
print(f"talk.politics.guns Model now finished, time use {used_time} seconds")
save(f17, filename17)

m18 = CountFrequency('data_train/talk.politics.mideast')
print(f"Training talk.politics.mideast Model")
start = time.time()
m18.catch_data()
m18.break_data()
f18 = m18.frequency_counter()
f18 = adjust_frequency(f18)
end = time.time()
used_time = end - start
print(f"talk.politics.mideast Model now finished, time use {used_time} seconds")
save(f18, filename18)

m19 = CountFrequency('data_train/talk.politics.misc')
print(f"Training talk.politics.misc Model")
start = time.time()
m19.catch_data()
m19.break_data()
f19 = m19.frequency_counter()
f19 = adjust_frequency(f19)
end = time.time()
used_time = end - start
print(f"talk.politics.misc Model now finished, time use {used_time} seconds")
save(f19, filename19)

m20 = CountFrequency('data_train/talk.religion.misc')
print(f"Training talk.religion.misc Model")
start = time.time()
m20.catch_data()
m20.break_data()
f20 = m20.frequency_counter()
f20 = adjust_frequency(f20)
end = time.time()
used_time = end - start
print(f"talk.religion.misc Model now finished, time use {used_time} seconds")
save(f20, filename20)


total_end = time.time()
total_time = total_end - total_start

print(f"The training process has been done, total time use: {total_time} seconds")

