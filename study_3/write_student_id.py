import requests
import pymysql
import random

def rand_student_id():
	
	second_seed="5678"
	seed="0123456789"
	all_num=''
	second=random.choice(second_seed)
	for i in range(0,7):
		rand_num=random.choice(seed)
		all_num+=rand_num
	all_num='1'+second+all_num
	return all_num

def rand_student_name():
	first_seed="赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛"
	second_seed="伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛"
	third_seed="昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善庆磊民友裕河哲江超浩亮"
	first=random.choice(first_seed)
	second=random.choice(second_seed)
	third=random.choice(third_seed)
	name=first+second+third
	return name
def connect_db():

	db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='learning')
	cursor=db.cursor()
	return db,cursor

def main():
	db,cursor=connect_db()
	sql="select * from books"
	result=cursor.execute(sql)

	for i in range(100):
		user_id=rand_student_id()
		user_pwd="123456"
		user_name=rand_student_name()

		user_id=" '{}' ".format(user_id)
		user_pwd=" '{}' ".format(user_pwd)
		user_name=" '{}' ".format(user_name)

		sql="insert into user (user_id,user_pwd,user_name) value ({},{},{}) ".format(user_id,user_pwd,user_name)
		cursor.execute(sql)
	db.commit()
def now_borrow_books():
	info=[]
	db,cursor=connect_db()
	sql="select user_id from user "
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		one=i[0]
		info.append(one)
	return info

def books():
	info=[]
	db,cursor=connect_db()
	sql="select id from books "
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		one=i[0]
		info.append(one)
	return info

def ceshi():
	db,cursor=connect_db()
	# book=books()
	# user=now_borrow_books()
	book=[2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436, 2437, 2438, 2439, 2440, 2441, 2442, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2463, 2464, 2465, 2466, 2467, 2468, 2469, 2470, 2471, 2472, 2473, 2474, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2493, 2494, 2495, 2496, 2497, 2498, 2499, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2512, 2513, 2514, 2515, 2516, 2517, 2518, 2519, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 2527, 2528, 2529, 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618, 2619, 2620, 2621, 2622, 2623, 2624, 2625, 2626, 2627, 2628, 2629, 2630, 2631, 2632, 2633, 2634, 2635, 2636, 2637, 2638, 2639, 2640, 2641, 2642, 2643, 2644, 2645, 2646, 2647, 2648, 2649, 2650, 2651, 2652, 2653, 2654, 2655, 2656, 2657, 2658, 2659, 2660, 2661, 2662, 2663, 2664, 2665, 2666, 2667, 2668, 2669, 2670, 2671, 2672, 2673, 2674, 2675, 2676, 2677, 2678, 2679, 2680, 2681, 2682, 2683, 2684, 2685, 2686, 2687, 2688, 2689, 2690, 2691, 2692, 2693, 2694, 2695, 2696, 2697, 2698, 2699, 2700, 2701, 2702, 2703, 2704, 2705, 2706, 2707, 2708, 2709, 2710, 2711, 2712, 2713, 2714, 2715, 2716, 2717, 2718, 2719, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2765, 2766, 2767, 2768, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2784, 2785, 2786, 2787, 2788, 2789, 2790, 2791, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844, 2845, 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867, 2868, 2869, 2870, 2871, 2872, 2873, 2874, 2875, 2876, 2877, 2878, 2879, 2880, 2881, 2882, 2883, 2884, 2885, 2886, 2887, 2888, 2889, 2890, 2891, 2892, 2893, 2894, 2895, 2896, 2897, 2898, 2899, 2900, 2901, 2902, 2903, 2904, 2905, 2906, 2907, 2908, 2909, 2910, 2911, 2912, 2913, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2924, 2925, 2926, 2927, 2928, 2929, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2937, 2938, 2939, 2940, 2941, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2951, 2952, 2953, 2954, 2955, 2956, 2957, 2958, 2959, 2960, 2961, 2962, 2963, 2964, 2965, 2966, 2967, 2968, 2969, 2970, 2971, 2972, 2973, 2974, 2975, 2976, 2977, 2978, 2979, 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3079, 3080, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3110, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3120, 3121]
	user=[150927926, 151268791, 151925582, 152470097, 153301218, 153366002, 153414679, 153416520, 153884206, 156250105, 156404715, 156450454, 156982473, 157958326, 158460799, 158592278, 159306309, 159586892, 161627033, 161729286, 162031260, 162928712, 163206056, 163451107, 163752469, 164205796, 164863989, 165120606, 165609576, 165618513, 166286135, 166444193, 166593931, 166651393, 166786450, 166982580, 167648656, 168123289, 168467872, 168829364, 168929169, 169012977, 169195584, 169251513, 169553356, 170368361, 171097378, 171526542, 172927629, 173356691, 174375022, 175094720, 175401728, 175621318, 175861433, 176074548, 176137561, 176423122, 176670563, 176777166, 176840047, 177145930, 177181885, 178081034, 178476105, 179736170, 179762265, 180434768, 180634722, 180659892, 180957743, 181447776, 181614532, 181628693, 181958371, 181992171, 182772274, 182969334, 183046203, 183264905, 183297570, 183394742, 183620403, 183730102, 186056261, 186097686, 186478459, 186612301, 187165101, 187376912, 187565280, 187994258, 188080589, 188276729, 188319213, 188774390, 188842301, 189295995, 189738522, 189960997]

	book=random.sample(book,80)
	user=random.sample(user,80)
	db,cursor=connect_db()
	for i in range(0,81):
		now_borrow2=book[i]
		now_borrow3=" '{}' ".format(now_borrow2)

		now_borrow_books2=user[i]
		now_borrow_books3=" '{}' ".format(now_borrow_books2)
		
		# sql1="insert into books (now_borrow) values ({})  where id={} ;".format(now_borrow_books3,now_borrow2)
		sql1="UPDATE books SET now_borrow={} where id={} ".format(now_borrow_books3,now_borrow2)
		#sql2="insert into user (now_borrow_books) values ({}) where user_id={} ;".format(now_borrow3,now_borrow_books2)
		sql2="UPDATE user SET now_borrow_books={} where user_id={} ".format(now_borrow3,now_borrow_books2)

		print(sql1)
		print(sql2)
		cursor.execute(sql1)
		cursor.execute(sql2)
		db.commit()
def write_sex():
	db,cursor=connect_db()
	sql="select user_id from user "
	cursor.execute(sql)
	result=cursor.fetchall()
	db.commit()
	sexs='男女'
	for i in result:
		sex=random.choice(sexs)
		sex=" '{}' ".format(sex)
		sql="UPDATE user SET user_sex={} where user_id={} ".format(sex,i[0])
		cursor.execute(sql)
	db.commit()
def write_tele():
	db,cursor=connect_db()
	sql="select user_id from user "
	cursor.execute(sql)
	result=cursor.fetchall()

	second='3857'
	third='0123456789'
	for i in result:
		id=i[0]
		tele=''
		two=random.choice(second)
		for i in range(0,9):
			tele+=random.choice(third)
		tele='1'+two+tele
		tele="'{}'".format(tele)
		sql="UPDATE user SET user_tele={} where user_id={} ".format(tele,id)
		cursor.execute(sql)
	db.commit()

def delete_info():
	db,cursor=connect_db()
	sql="delete from books_copy where status=0 ";
	result=cursor.execute(sql)
	db.commit()
	print(result)

delete_info()

