% Generated facts by the python script
_class(film2332, film2332HN1, [mon], 1600, 1845).
_class(film2332, film2332001, [mon], 1600, 1845).
_class(govt2305, govt2305001, [mon, wed, fri], 1300, 1350).
_class(govt2305, govt2305002, [mon, wed, fri], 1000, 1050).
_class(govt2305, govt2305003, [mon, wed, fri], 1600, 1650).
_class(cs4337, cs4337HON, [mon, wed], 1600, 1715).
_class(cs4337, cs4337002, [tues, thurs], 1600, 1715).
_class(cs4337, cs4337001, [mon, wed], 1000, 1115).
_class(cs4337, cs4337501, [tues, thurs], 1730, 1845).
_class(cs3345, cs3345002, [mon, wed], 1600, 1715).
_class(cs3345, cs3345004, [tues, thurs], 830, 945).
_class(cs3345, cs3345003, [mon, wed], 1130, 1245).
_class(cs3345, cs3345001, [mon, wed], 1000, 1115).
_class(cs3345, cs3345005, [mon, wed], 830, 945).
_class(cs3345, cs3345501, [tues, thurs], 1900, 2015).
_class(cs4341, cs4341HON, [mon, wed], 1000, 1115).
_class(cs4341, cs4341001, [mon, wed], 1300, 1415).
_class(cs4341, cs4341002, [tues, thurs], 1430, 1545).
_class(cs4341, cs4341003, [mon, wed], 1430, 1545).

% Include the rules in a separate file
#include 'schedule.lp'.

% Generated query to generate the schedule
?- _main([film2332, govt2305, cs4337, cs4437, cs3345, cs4341]).