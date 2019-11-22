import timeit







rang = 1000
lst = list(range(rang))

# with open('test', 'w') as file:
#     for item in lst:
#         file.write(f' lst[{item}] or')

def any_test():
    if any(lst):
        return True
    return False

def or_test():
    if lst[0] or lst[1] or lst[2] or lst[3] or lst[4] or lst[5] or lst[6] or lst[7] or lst[8] or lst[9] or lst[10] or lst[11] or lst[12] or lst[13] or lst[14] or lst[15] or lst[16] or lst[17] or lst[18] or lst[19] or lst[20] or lst[21] or lst[22] or lst[23] or lst[24] or lst[25] or lst[26] or lst[27] or lst[28] or lst[29] or lst[30] or lst[31] or lst[32] or lst[33] or lst[34] or lst[35] or lst[36] or lst[37] or lst[38] or lst[39] or lst[40] or lst[41] or lst[42] or lst[43] or lst[44] or lst[45] or lst[46] or lst[47] or lst[48] or lst[49] or lst[50] or lst[51] or lst[52] or lst[53] or lst[54] or lst[55] or lst[56] or lst[57] or lst[58] or lst[59] or lst[60] or lst[61] or lst[62] or lst[63] or lst[64] or lst[65] or lst[66] or lst[67] or lst[68] or lst[69] or lst[70] or lst[71] or lst[72] or lst[73] or lst[74] or lst[75] or lst[76] or lst[77] or lst[78] or lst[79] or lst[80] or lst[81] or lst[82] or lst[83] or lst[84] or lst[85] or lst[86] or lst[87] or lst[88] or lst[89] or lst[90] or lst[91] or lst[92] or lst[93] or lst[94] or lst[95] or lst[96] or lst[97] or lst[98] or lst[99] or lst[100] or lst[101] or lst[102] or lst[103] or lst[104] or lst[105] or lst[106] or lst[107] or lst[108] or lst[109] or lst[110] or lst[111] or lst[112] or lst[113] or lst[114] or lst[115] or lst[116] or lst[117] or lst[118] or lst[119] or lst[120] or lst[121] or lst[122] or lst[123] or lst[124] or lst[125] or lst[126] or lst[127] or lst[128] or lst[129] or lst[130] or lst[131] or lst[132] or lst[133] or lst[134] or lst[135] or lst[136] or lst[137] or lst[138] or lst[139] or lst[140] or lst[141] or lst[142] or lst[143] or lst[144] or lst[145] or lst[146] or lst[147] or lst[148] or lst[149] or lst[150] or lst[151] or lst[152] or lst[153] or lst[154] or lst[155] or lst[156] or lst[157] or lst[158] or lst[159] or lst[160] or lst[161] or lst[162] or lst[163] or lst[164] or lst[165] or lst[166] or lst[167] or lst[168] or lst[169] or lst[170] or lst[171] or lst[172] or lst[173] or lst[174] or lst[175] or lst[176] or lst[177] or lst[178] or lst[179] or lst[180] or lst[181] or lst[182] or lst[183] or lst[184] or lst[185] or lst[186] or lst[187] or lst[188] or lst[189] or lst[190] or lst[191] or lst[192] or lst[193] or lst[194] or lst[195] or lst[196] or lst[197] or lst[198] or lst[199] or lst[200] or lst[201] or lst[202] or lst[203] or lst[204] or lst[205] or lst[206] or lst[207] or lst[208] or lst[209] or lst[210] or lst[211] or lst[212] or lst[213] or lst[214] or lst[215] or lst[216] or lst[217] or lst[218] or lst[219] or lst[220] or lst[221] or lst[222] or lst[223] or lst[224] or lst[225] or lst[226] or lst[227] or lst[228] or lst[229] or lst[230] or lst[231] or lst[232] or lst[233] or lst[234] or lst[235] or lst[236] or lst[237] or lst[238] or lst[239] or lst[240] or lst[241] or lst[242] or lst[243] or lst[244] or lst[245] or lst[246] or lst[247] or lst[248] or lst[249] or lst[250] or lst[251] or lst[252] or lst[253] or lst[254] or lst[255] or lst[256] or lst[257] or lst[258] or lst[259] or lst[260] or lst[261] or lst[262] or lst[263] or lst[264] or lst[265] or lst[266] or lst[267] or lst[268] or lst[269] or lst[270] or lst[271] or lst[272] or lst[273] or lst[274] or lst[275] or lst[276] or lst[277] or lst[278] or lst[279] or lst[280] or lst[281] or lst[282] or lst[283] or lst[284] or lst[285] or lst[286] or lst[287] or lst[288] or lst[289] or lst[290] or lst[291] or lst[292] or lst[293] or lst[294] or lst[295] or lst[296] or lst[297] or lst[298] or lst[299] or lst[300] or lst[301] or lst[302] or lst[303] or lst[304] or lst[305] or lst[306] or lst[307] or lst[308] or lst[309] or lst[310] or lst[311] or lst[312] or lst[313] or lst[314] or lst[315] or lst[316] or lst[317] or lst[318] or lst[319] or lst[320] or lst[321] or lst[322] or lst[323] or lst[324] or lst[325] or lst[326] or lst[327] or lst[328] or lst[329] or lst[330] or lst[331] or lst[332] or lst[333] or lst[334] or lst[335] or lst[336] or lst[337] or lst[338] or lst[339] or lst[340] or lst[341] or lst[342] or lst[343] or lst[344] or lst[345] or lst[346] or lst[347] or lst[348] or lst[349] or lst[350] or lst[351] or lst[352] or lst[353] or lst[354] or lst[355] or lst[356] or lst[357] or lst[358] or lst[359] or lst[360] or lst[361] or lst[362] or lst[363] or lst[364] or lst[365] or lst[366] or lst[367] or lst[368] or lst[369] or lst[370] or lst[371] or lst[372] or lst[373] or lst[374] or lst[375] or lst[376] or lst[377] or lst[378] or lst[379] or lst[380] or lst[381] or lst[382] or lst[383] or lst[384] or lst[385] or lst[386] or lst[387] or lst[388] or lst[389] or lst[390] or lst[391] or lst[392] or lst[393] or lst[394] or lst[395] or lst[396] or lst[397] or lst[398] or lst[399] or lst[400] or lst[401] or lst[402] or lst[403] or lst[404] or lst[405] or lst[406] or lst[407] or lst[408] or lst[409] or lst[410] or lst[411] or lst[412] or lst[413] or lst[414] or lst[415] or lst[416] or lst[417] or lst[418] or lst[419] or lst[420] or lst[421] or lst[422] or lst[423] or lst[424] or lst[425] or lst[426] or lst[427] or lst[428] or lst[429] or lst[430] or lst[431] or lst[432] or lst[433] or lst[434] or lst[435] or lst[436] or lst[437] or lst[438] or lst[439] or lst[440] or lst[441] or lst[442] or lst[443] or lst[444] or lst[445] or lst[446] or lst[447] or lst[448] or lst[449] or lst[450] or lst[451] or lst[452] or lst[453] or lst[454] or lst[455] or lst[456] or lst[457] or lst[458] or lst[459] or lst[460] or lst[461] or lst[462] or lst[463] or lst[464] or lst[465] or lst[466] or lst[467] or lst[468] or lst[469] or lst[470] or lst[471] or lst[472] or lst[473] or lst[474] or lst[475] or lst[476] or lst[477] or lst[478] or lst[479] or lst[480] or lst[481] or lst[482] or lst[483] or lst[484] or lst[485] or lst[486] or lst[487] or lst[488] or lst[489] or lst[490] or lst[491] or lst[492] or lst[493] or lst[494] or lst[495] or lst[496] or lst[497] or lst[498] or lst[499] or lst[500] or lst[501] or lst[502] or lst[503] or lst[504] or lst[505] or lst[506] or lst[507] or lst[508] or lst[509] or lst[510] or lst[511] or lst[512] or lst[513] or lst[514] or lst[515] or lst[516] or lst[517] or lst[518] or lst[519] or lst[520] or lst[521] or lst[522] or lst[523] or lst[524] or lst[525] or lst[526] or lst[527] or lst[528] or lst[529] or lst[530] or lst[531] or lst[532] or lst[533] or lst[534] or lst[535] or lst[536] or lst[537] or lst[538] or lst[539] or lst[540] or lst[541] or lst[542] or lst[543] or lst[544] or lst[545] or lst[546] or lst[547] or lst[548] or lst[549] or lst[550] or lst[551] or lst[552] or lst[553] or lst[554] or lst[555] or lst[556] or lst[557] or lst[558] or lst[559] or lst[560] or lst[561] or lst[562] or lst[563] or lst[564] or lst[565] or lst[566] or lst[567] or lst[568] or lst[569] or lst[570] or lst[571] or lst[572] or lst[573] or lst[574] or lst[575] or lst[576] or lst[577] or lst[578] or lst[579] or lst[580] or lst[581] or lst[582] or lst[583] or lst[584] or lst[585] or lst[586] or lst[587] or lst[588] or lst[589] or lst[590] or lst[591] or lst[592] or lst[593] or lst[594] or lst[595] or lst[596] or lst[597] or lst[598] or lst[599] or lst[600] or lst[601] or lst[602] or lst[603] or lst[604] or lst[605] or lst[606] or lst[607] or lst[608] or lst[609] or lst[610] or lst[611] or lst[612] or lst[613] or lst[614] or lst[615] or lst[616] or lst[617] or lst[618] or lst[619] or lst[620] or lst[621] or lst[622] or lst[623] or lst[624] or lst[625] or lst[626] or lst[627] or lst[628] or lst[629] or lst[630] or lst[631] or lst[632] or lst[633] or lst[634] or lst[635] or lst[636] or lst[637] or lst[638] or lst[639] or lst[640] or lst[641] or lst[642] or lst[643] or lst[644] or lst[645] or lst[646] or lst[647] or lst[648] or lst[649] or lst[650] or lst[651] or lst[652] or lst[653] or lst[654] or lst[655] or lst[656] or lst[657] or lst[658] or lst[659] or lst[660] or lst[661] or lst[662] or lst[663] or lst[664] or lst[665] or lst[666] or lst[667] or lst[668] or lst[669] or lst[670] or lst[671] or lst[672] or lst[673] or lst[674] or lst[675] or lst[676] or lst[677] or lst[678] or lst[679] or lst[680] or lst[681] or lst[682] or lst[683] or lst[684] or lst[685] or lst[686] or lst[687] or lst[688] or lst[689] or lst[690] or lst[691] or lst[692] or lst[693] or lst[694] or lst[695] or lst[696] or lst[697] or lst[698] or lst[699] or lst[700] or lst[701] or lst[702] or lst[703] or lst[704] or lst[705] or lst[706] or lst[707] or lst[708] or lst[709] or lst[710] or lst[711] or lst[712] or lst[713] or lst[714] or lst[715] or lst[716] or lst[717] or lst[718] or lst[719] or lst[720] or lst[721] or lst[722] or lst[723] or lst[724] or lst[725] or lst[726] or lst[727] or lst[728] or lst[729] or lst[730] or lst[731] or lst[732] or lst[733] or lst[734] or lst[735] or lst[736] or lst[737] or lst[738] or lst[739] or lst[740] or lst[741] or lst[742] or lst[743] or lst[744] or lst[745] or lst[746] or lst[747] or lst[748] or lst[749] or lst[750] or lst[751] or lst[752] or lst[753] or lst[754] or lst[755] or lst[756] or lst[757] or lst[758] or lst[759] or lst[760] or lst[761] or lst[762] or lst[763] or lst[764] or lst[765] or lst[766] or lst[767] or lst[768] or lst[769] or lst[770] or lst[771] or lst[772] or lst[773] or lst[774] or lst[775] or lst[776] or lst[777] or lst[778] or lst[779] or lst[780] or lst[781] or lst[782] or lst[783] or lst[784] or lst[785] or lst[786] or lst[787] or lst[788] or lst[789] or lst[790] or lst[791] or lst[792] or lst[793] or lst[794] or lst[795] or lst[796] or lst[797] or lst[798] or lst[799] or lst[800] or lst[801] or lst[802] or lst[803] or lst[804] or lst[805] or lst[806] or lst[807] or lst[808] or lst[809] or lst[810] or lst[811] or lst[812] or lst[813] or lst[814] or lst[815] or lst[816] or lst[817] or lst[818] or lst[819] or lst[820] or lst[821] or lst[822] or lst[823] or lst[824] or lst[825] or lst[826] or lst[827] or lst[828] or lst[829] or lst[830] or lst[831] or lst[832] or lst[833] or lst[834] or lst[835] or lst[836] or lst[837] or lst[838] or lst[839] or lst[840] or lst[841] or lst[842] or lst[843] or lst[844] or lst[845] or lst[846] or lst[847] or lst[848] or lst[849] or lst[850] or lst[851] or lst[852] or lst[853] or lst[854] or lst[855] or lst[856] or lst[857] or lst[858] or lst[859] or lst[860] or lst[861] or lst[862] or lst[863] or lst[864] or lst[865] or lst[866] or lst[867] or lst[868] or lst[869] or lst[870] or lst[871] or lst[872] or lst[873] or lst[874] or lst[875] or lst[876] or lst[877] or lst[878] or lst[879] or lst[880] or lst[881] or lst[882] or lst[883] or lst[884] or lst[885] or lst[886] or lst[887] or lst[888] or lst[889] or lst[890] or lst[891] or lst[892] or lst[893] or lst[894] or lst[895] or lst[896] or lst[897] or lst[898] or lst[899] or lst[900] or lst[901] or lst[902] or lst[903] or lst[904] or lst[905] or lst[906] or lst[907] or lst[908] or lst[909] or lst[910] or lst[911] or lst[912] or lst[913] or lst[914] or lst[915] or lst[916] or lst[917] or lst[918] or lst[919] or lst[920] or lst[921] or lst[922] or lst[923] or lst[924] or lst[925] or lst[926] or lst[927] or lst[928] or lst[929] or lst[930] or lst[931] or lst[932] or lst[933] or lst[934] or lst[935] or lst[936] or lst[937] or lst[938] or lst[939] or lst[940] or lst[941] or lst[942] or lst[943] or lst[944] or lst[945] or lst[946] or lst[947] or lst[948] or lst[949] or lst[950] or lst[951] or lst[952] or lst[953] or lst[954] or lst[955] or lst[956] or lst[957] or lst[958] or lst[959] or lst[960] or lst[961] or lst[962] or lst[963] or lst[964] or lst[965] or lst[966] or lst[967] or lst[968] or lst[969] or lst[970] or lst[971] or lst[972] or lst[973] or lst[974] or lst[975] or lst[976] or lst[977] or lst[978] or lst[979] or lst[980] or lst[981] or lst[982] or lst[983] or lst[984] or lst[985] or lst[986] or lst[987] or lst[988] or lst[989] or lst[990] or lst[991] or lst[992] or lst[993] or lst[994] or lst[995] or lst[996] or lst[997] or lst[998] or lst[999]:
        return True
    return False

def reference():
    if lst[0]:
        return True
    return False

def my_implementation():
    for item in lst:
        if item:
            return True
    return False

def test_suite():
    num, rep = 100_000, 100
    print(f'range = {rang:_}, num = {num:_}, rep = {rep:_}')
    print(f'any_test >> {min(timeit.repeat(any_test, number=num, repeat=rep)):0.4f}s')
    print(f'or_test >> {min(timeit.repeat(or_test, number=num, repeat=rep)):0.4f}s')
    print(f'reference_test >> {min(timeit.repeat(reference, number=num, repeat=rep)):0.4f}s')
    print(f'my_implementation_test >> {min(timeit.repeat(my_implementation, number=num, repeat=rep)):0.4f}s')


test_suite()

# result = list_test()
'''
range = 1_000, num, rep = 1, 1
any_test >> 0.0000s
or_test >> 0.0000s

range = 1_000, num, rep = 1_000_000, 1
any_test >> 0.1561s
or_test >> 0.1399s

range = 1_000, num, rep = 1_000_000, 10
any_test >> 0.1567s
or_test >> 0.1426s

range = 1_000, num = 10_000, rep = 100
any_test >> 0.0015s
or_test >> 0.0014s

range = 1_000, num = 100_000, rep = 100
any_test >> 0.0152s
or_test >> 0.0139s
reference_test >> 0.0099s
'''