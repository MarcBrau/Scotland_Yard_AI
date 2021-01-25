edges_original = [(1, 8, {"type": "taxi"}),
                  (1, 9, {"type": "taxi"}),
                  (1, 58, {"type": "bus"}),
                  (1, 46, {"type": "bus"}),
                  (1, 46, {"type": "metro"}),
                  (2, 10, {"type": "taxi"}),
                  (2, 20, {"type": "taxi"}),
                  (3, 4, {"type": "taxi"}),
                  (3, 11, {"type": "taxi"}),
                  (3, 12, {"type": "taxi"}),
                  (3, 22, {"type": "bus"}),
                  (3, 23, {"type": "bus"}),
                  (4, 13, {"type": "taxi"}),
                  (5, 15, {"type": "taxi"}),
                  (5, 16, {"type": "taxi"}),
                  (6, 7, {"type": "taxi"}),
                  (6, 29, {"type": "taxi"}),
                  (7, 17, {"type": "taxi"}),
                  (7, 42, {"type": "bus"}),
                  (8, 18, {"type": "taxi"}),
                  (8, 19, {"type": "taxi"}),
                  (9, 19, {"type": "taxi"}),
                  (9, 20, {"type": "taxi"}),
                  (10, 11, {"type": "taxi"}),
                  (10, 21, {"type": "taxi"}),
                  (11, 22, {"type": "taxi"}),
                  (12, 23, {"type": "taxi"}),
                  (13, 14, {"type": "bus"}),
                  (13, 23, {"type": "taxi"}),
                  (13, 23, {"type": "bus"}),
                  (13, 24, {"type": "taxi"}),
                  (13, 46, {"type": "metro"}),
                  (13, 52, {"type": "bus"}),
                  (13, 67, {"type": "metro"}),
                  (13, 89, {"type": "metro"}),
                  (14, 15, {"type": "taxi"}),
                  (14, 15, {"type": "bus"}),
                  (14, 25, {"type": "taxi"}),
                  (14, 52, {"type": "bus"}),
                  (15, 16, {"type": "taxi"}),
                  (15, 26, {"type": "taxi"}),
                  (15, 28, {"type": "taxi"}),
                  (15, 29, {"type": "bus"}),
                  (15, 41, {"type": "bus"}),
                  (16, 28, {"type": "taxi"}),
                  (16, 29, {"type": "taxi"}),
                  (17, 29, {"type": "taxi"}),
                  (17, 30, {"type": "taxi"}),
                  (18, 31, {"type": "taxi"}),
                  (18, 43, {"type": "taxi"}),
                  (19, 32, {"type": "taxi"}),
                  (20, 33, {"type": "taxi"}),
                  (21, 33, {"type": "taxi"}),
                  (22, 23, {"type": "taxi"}),
                  (22, 23, {"type": "bus"}),
                  (22, 34, {"type": "taxi"}),
                  (22, 34, {"type": "bus"}),
                  (22, 35, {"type": "taxi"}),
                  (22, 65, {"type": "bus"}),
                  (23, 37, {"type": "taxi"}),
                  (23, 67, {"type": "bus"}),
                  (24, 37, {"type": "taxi"}),
                  (24, 38, {"type": "taxi"}),
                  (25, 38, {"type": "taxi"}),
                  (25, 39, {"type": "taxi"}),
                  (26, 27, {"type": "taxi"}),
                  (26, 39, {"type": "taxi"}),
                  (27, 28, {"type": "taxi"}),
                  (27, 40, {"type": "taxi"}),
                  (28, 41, {"type": "taxi"}),
                  (29, 41, {"type": "taxi"}),
                  (29, 41, {"type": "bus"}),
                  (29, 42, {"type": "taxi"}),
                  (29, 42, {"type": "bus"}),
                  (29, 55, {"type": "bus"}),
                  (29, 89, {"type": "metro"}),
                  (30, 42, {"type": "taxi"}),
                  (31, 43, {"type": "taxi"}),
                  (31, 44, {"type": "taxi"}),
                  (32, 33, {"type": "taxi"}),
                  (32, 44, {"type": "taxi"}),
                  (32, 45, {"type": "taxi"}),
                  (33, 46, {"type": "taxi"}),
                  (34, 46, {"type": "bus"}),
                  (34, 47, {"type": "taxi"}),
                  (34, 48, {"type": "taxi"}),
                  (34, 63, {"type": "bus"}),
                  (35, 36, {"type": "taxi"}),
                  (35, 48, {"type": "taxi"}),
                  (35, 65, {"type": "taxi"}),
                  (36, 37, {"type": "taxi"}),
                  (36, 49, {"type": "taxi"}),
                  (37, 50, {"type": "taxi"}),
                  (38, 50, {"type": "taxi"}),
                  (38, 51, {"type": "taxi"}),
                  (39, 51, {"type": "taxi"}),
                  (39, 52, {"type": "taxi"}),
                  (40, 41, {"type": "taxi"}),
                  (40, 52, {"type": "taxi"}),
                  (40, 53, {"type": "taxi"}),
                  (41, 52, {"type": "bus"}),
                  (41, 54, {"type": "taxi"}),
                  (41, 87, {"type": "bus"}),
                  (42, 56, {"type": "taxi"}),
                  (42, 72, {"type": "taxi"}),
                  (42, 72, {"type": "bus"}),
                  (43, 57, {"type": "taxi"}),
                  (44, 58, {"type": "taxi"}),
                  (45, 46, {"type": "taxi"}),
                  (45, 58, {"type": "taxi"}),
                  (45, 59, {"type": "taxi"}),
                  (45, 60, {"type": "taxi"}),
                  (46, 47, {"type": "taxi"}),
                  (46, 58, {"type": "bus"}),
                  (46, 61, {"type": "taxi"}),
                  (46, 74, {"type": "metro"}),
                  (46, 78, {"type": "bus"}),
                  (46, 79, {"type": "metro"}),
                  (47, 62, {"type": "taxi"}),
                  (48, 62, {"type": "taxi"}),
                  (48, 63, {"type": "taxi"}),
                  (49, 50, {"type": "taxi"}),
                  (49, 66, {"type": "taxi"}),
                  (51, 52, {"type": "taxi"}),
                  (51, 67, {"type": "taxi"}),
                  (51, 68, {"type": "taxi"}),
                  (52, 67, {"type": "bus"}),
                  (52, 69, {"type": "taxi"}),
                  (52, 86, {"type": "bus"}),
                  (53, 54, {"type": "taxi"}),
                  (53, 69, {"type": "taxi"}),
                  (54, 55, {"type": "taxi"}),
                  (54, 70, {"type": "taxi"}),
                  (55, 71, {"type": "taxi"}),
                  (55, 89, {"type": "bus"}),
                  (56, 91, {"type": "taxi"}),
                  (57, 58, {"type": "taxi"}),
                  (57, 73, {"type": "taxi"}),
                  (58, 59, {"type": "taxi"}),
                  (58, 74, {"type": "taxi"}),
                  (58, 74, {"type": "bus"}),
                  (58, 75, {"type": "taxi"}),
                  (58, 77, {"type": "bus"}),
                  (59, 75, {"type": "taxi"}),
                  (59, 76, {"type": "taxi"}),
                  (60, 61, {"type": "taxi"}),
                  (60, 76, {"type": "taxi"}),
                  (61, 62, {"type": "taxi"}),
                  (61, 76, {"type": "taxi"}),
                  (61, 78, {"type": "taxi"}),
                  (62, 79, {"type": "taxi"}),
                  (63, 64, {"type": "taxi"}),
                  (63, 65, {"type": "bus"}),
                  (63, 80, {"type": "taxi"}),
                  (63, 100, {"type": "bus"}),
                  (64, 65, {"type": "taxi"}),
                  (64, 81, {"type": "taxi"}),
                  (65, 66, {"type": "taxi"}),
                  (65, 67, {"type": "bus"}),
                  (65, 82, {"type": "taxi"}),
                  (65, 82, {"type": "bus"}),
                  (66, 67, {"type": "taxi"}),
                  (66, 82, {"type": "taxi"}),
                  (67, 68, {"type": "taxi"}),
                  (67, 82, {"type": "bus"}),
                  (67, 84, {"type": "taxi"}),
                  (67, 79, {"type": "metro"}),
                  (67, 89, {"type": "metro"}),
                  (67, 102, {"type": "bus"}),
                  (67, 111, {"type": "metro"}),
                  (68, 69, {"type": "taxi"}),
                  (68, 85, {"type": "taxi"}),
                  (69, 86, {"type": "taxi"}),
                  (70, 71, {"type": "taxi"}),
                  (70, 87, {"type": "taxi"}),
                  (71, 72, {"type": "taxi"}),
                  (71, 89, {"type": "taxi"}),
                  (72, 90, {"type": "taxi"}),
                  (72, 91, {"type": "taxi"}),
                  (72, 105, {"type": "bus"}),
                  (72, 107, {"type": "bus"}),
                  (73, 74, {"type": "taxi"}),
                  (73, 92, {"type": "taxi"}),
                  (74, 75, {"type": "taxi"}),
                  (74, 92, {"type": "taxi"}),
                  (74, 94, {"type": "bus"}),
                  (75, 94, {"type": "taxi"}),
                  (76, 77, {"type": "taxi"}),
                  (77, 78, {"type": "taxi"}),
                  (77, 78, {"type": "bus"}),
                  (77, 94, {"type": "bus"}),
                  (77, 95, {"type": "taxi"}),
                  (77, 96, {"type": "taxi"}),
                  (77, 124, {"type": "bus"}),
                  (78, 79, {"type": "taxi"}),
                  (78, 79, {"type": "bus"}),
                  (78, 97, {"type": "taxi"}),
                  (79, 93, {"type": "metro"}),
                  (79, 98, {"type": "taxi"}),
                  (79, 111, {"type": "metro"}),
                  (80, 99, {"type": "taxi"}),
                  (80, 100, {"type": "taxi"}),
                  (81, 82, {"type": "taxi"}),
                  (81, 100, {"type": "taxi"}),
                  (82, 101, {"type": "taxi"}),
                  (82, 140, {"type": "bus"}),
                  (83, 101, {"type": "taxi"}),
                  (83, 102, {"type": "taxi"}),
                  (84, 85, {"type": "taxi"}),
                  (85, 103, {"type": "taxi"}),
                  (86, 87, {"type": "bus"}),
                  (86, 102, {"type": "bus"}),
                  (86, 103, {"type": "taxi"}),
                  (86, 104, {"type": "taxi"}),
                  (86, 116, {"type": "bus"}),
                  (87, 88, {"type": "taxi"}),
                  (87, 105, {"type": "bus"}),
                  (88, 89, {"type": "taxi"}),
                  (88, 117, {"type": "taxi"}),
                  (89, 105, {"type": "taxi"}),
                  (89, 105, {"type": "bus"}),
                  (89, 128, {"type": "metro"}),
                  (89, 140, {"type": "metro"}),
                  (90, 91, {"type": "taxi"}),
                  (90, 105, {"type": "taxi"}),
                  (91, 105, {"type": "taxi"}),
                  (91, 107, {"type": "taxi"}),
                  (92, 93, {"type": "taxi"}),
                  (93, 94, {"type": "taxi"}),
                  (93, 94, {"type": "bus"}),
                  (94, 95, {"type": "taxi"}),
                  (95, 122, {"type": "taxi"}),
                  (96, 97, {"type": "taxi"}),
                  (96, 109, {"type": "taxi"}),
                  (97, 98, {"type": "taxi"}),
                  (97, 109, {"type": "taxi"}),
                  (98, 99, {"type": "taxi"}),
                  (98, 110, {"type": "taxi"}),
                  (99, 110, {"type": "taxi"}),
                  (99, 112, {"type": "taxi"}),
                  (100, 101, {"type": "taxi"}),
                  (100, 111, {"type": "bus"}),
                  (100, 112, {"type": "taxi"}),
                  (100, 113, {"type": "taxi"}),
                  (101, 114, {"type": "taxi"}),
                  (102, 103, {"type": "taxi"}),
                  (102, 115, {"type": "taxi"}),
                  (102, 127, {"type": "taxi"}),
                  (104, 116, {"type": "taxi"}),
                  (105, 106, {"type": "taxi"}),
                  (105, 107, {"type": "bus"}),
                  (105, 108, {"type": "taxi"}),
                  (105, 108, {"type": "bus"}),
                  (106, 107, {"type": "taxi"}),
                  (107, 119, {"type": "taxi"}),
                  (107, 161, {"type": "bus"}),
                  (108, 115, {"type": "ferry"}),
                  (108, 116, {"type": "bus"}),
                  (108, 117, {"type": "taxi"}),
                  (108, 119, {"type": "taxi"}),
                  (108, 135, {"type": "bus"}),
                  (109, 110, {"type": "taxi"}),
                  (109, 124, {"type": "taxi"}),
                  (110, 111, {"type": "taxi"}),
                  (111, 112, {"type": "taxi"}),
                  (111, 124, {"type": "taxi"}),
                  (111, 124, {"type": "bus"}),
                  (111, 153, {"type": "metro"}),
                  (111, 163, {"type": "metro"}),
                  (112, 125, {"type": "taxi"}),
                  (113, 114, {"type": "taxi"}),
                  (113, 125, {"type": "taxi"}),
                  (114, 115, {"type": "taxi"}),
                  (114, 126, {"type": "taxi"}),
                  (114, 131, {"type": "taxi"}),
                  (114, 132, {"type": "taxi"}),
                  (115, 127, {"type": "taxi"}),
                  (115, 157, {"type": "ferry"}),
                  (116, 117, {"type": "taxi"}),
                  (116, 118, {"type": "taxi"}),
                  (116, 127, {"type": "taxi"}),
                  (116, 127, {"type": "bus"}),
                  (116, 142, {"type": "bus"}),
                  (117, 129, {"type": "taxi"}),
                  (118, 129, {"type": "taxi"}),
                  (118, 134, {"type": "taxi"}),
                  (118, 142, {"type": "taxi"}),
                  (119, 136, {"type": "taxi"}),
                  (120, 121, {"type": "taxi"}),
                  (120, 144, {"type": "taxi"}),
                  (121, 122, {"type": "taxi"}),
                  (121, 145, {"type": "taxi"}),
                  (122, 123, {"type": "taxi"}),
                  (122, 123, {"type": "bus"}),
                  (122, 144, {"type": "bus"}),
                  (122, 146, {"type": "taxi"}),
                  (123, 124, {"type": "taxi"}),
                  (123, 124, {"type": "bus"}),
                  (123, 137, {"type": "taxi"}),
                  (123, 144, {"type": "bus"}),
                  (123, 148, {"type": "taxi"}),
                  (123, 149, {"type": "taxi"}),
                  (123, 165, {"type": "bus"}),
                  (124, 138, {"type": "taxi"}),
                  (124, 153, {"type": "bus"}),
                  (125, 131, {"type": "taxi"}),
                  (126, 127, {"type": "taxi"}),
                  (126, 140, {"type": "taxi"}),
                  (127, 133, {"type": "taxi"}),
                  (127, 133, {"type": "bus"}),
                  (127, 134, {"type": "taxi"}),
                  (128, 135, {"type": "bus"}),
                  (128, 140, {"type": "metro"}),
                  (128, 142, {"type": "taxi"}),
                  (128, 142, {"type": "bus"}),
                  (128, 143, {"type": "taxi"}),
                  (128, 160, {"type": "taxi"}),
                  (128, 161, {"type": "bus"}),
                  (128, 172, {"type": "taxi"}),
                  (128, 185, {"type": "metro"}),
                  (128, 187, {"type": "bus"}),
                  (128, 188, {"type": "taxi"}),
                  (128, 199, {"type": "bus"}),
                  (129, 135, {"type": "taxi"}),
                  (129, 142, {"type": "taxi"}),
                  (129, 143, {"type": "taxi"}),
                  (130, 131, {"type": "taxi"}),
                  (130, 139, {"type": "taxi"}),
                  (132, 140, {"type": "taxi"}),
                  (133, 140, {"type": "taxi"}),
                  (133, 140, {"type": "bus"}),
                  (133, 141, {"type": "taxi"}),
                  (133, 157, {"type": "bus"}),
                  (134, 141, {"type": "taxi"}),
                  (134, 142, {"type": "taxi"}),
                  (135, 136, {"type": "taxi"}),
                  (135, 143, {"type": "taxi"}),
                  (135, 161, {"type": "taxi"}),
                  (135, 161, {"type": "bus"}),
                  (136, 162, {"type": "taxi"}),
                  (137, 147, {"type": "taxi"}),
                  (138, 150, {"type": "taxi"}),
                  (138, 152, {"type": "taxi"}),
                  (139, 140, {"type": "taxi"}),
                  (139, 153, {"type": "taxi"}),
                  (139, 154, {"type": "taxi"}),
                  (140, 153, {"type": "metro"}),
                  (140, 154, {"type": "taxi"}),
                  (140, 154, {"type": "bus"}),
                  (140, 156, {"type": "taxi"}),
                  (140, 156, {"type": "bus"}),
                  (141, 142, {"type": "taxi"}),
                  (141, 158, {"type": "taxi"}),
                  (142, 143, {"type": "taxi"}),
                  (142, 157, {"type": "bus"}),
                  (142, 158, {"type": "taxi"}),
                  (143, 160, {"type": "taxi"}),
                  (144, 145, {"type": "taxi"}),
                  (144, 163, {"type": "bus"}),
                  (144, 177, {"type": "taxi"}),
                  (145, 146, {"type": "taxi"}),
                  (146, 147, {"type": "taxi"}),
                  (146, 163, {"type": "taxi"}),
                  (147, 164, {"type": "taxi"}),
                  (148, 149, {"type": "taxi"}),
                  (148, 164, {"type": "taxi"}),
                  (149, 150, {"type": "taxi"}),
                  (149, 165, {"type": "taxi"}),
                  (150, 151, {"type": "taxi"}),
                  (151, 152, {"type": "taxi"}),
                  (151, 165, {"type": "taxi"}),
                  (151, 166, {"type": "taxi"}),
                  (152, 153, {"type": "taxi"}),
                  (153, 154, {"type": "taxi"}),
                  (153, 154, {"type": "bus"}),
                  (153, 163, {"type": "metro"}),
                  (153, 166, {"type": "taxi"}),
                  (153, 167, {"type": "taxi"}),
                  (153, 180, {"type": "bus"}),
                  (153, 184, {"type": "bus"}),
                  (153, 185, {"type": "metro"}),
                  (154, 155, {"type": "taxi"}),
                  (154, 156, {"type": "bus"}),
                  (155, 156, {"type": "taxi"}),
                  (155, 167, {"type": "taxi"}),
                  (155, 168, {"type": "taxi"}),
                  (156, 157, {"type": "taxi"}),
                  (156, 157, {"type": "bus"}),
                  (156, 169, {"type": "taxi"}),
                  (156, 184, {"type": "bus"}),
                  (157, 158, {"type": "taxi"}),
                  (157, 170, {"type": "taxi"}),
                  (157, 185, {"type": "bus"}),
                  (157, 194, {"type": "ferry"}),
                  (158, 159, {"type": "taxi"}),
                  (159, 170, {"type": "taxi"}),
                  (159, 172, {"type": "taxi"}),
                  (159, 186, {"type": "taxi"}),
                  (159, 198, {"type": "taxi"}),
                  (160, 161, {"type": "taxi"}),
                  (160, 173, {"type": "taxi"}),
                  (161, 174, {"type": "taxi"}),
                  (161, 199, {"type": "bus"}),
                  (162, 175, {"type": "taxi"}),
                  (163, 176, {"type": "bus"}),
                  (163, 177, {"type": "taxi"}),
                  (163, 191, {"type": "bus"}),
                  (164, 178, {"type": "taxi"}),
                  (164, 179, {"type": "taxi"}),
                  (165, 179, {"type": "taxi"}),
                  (165, 180, {"type": "taxi"}),
                  (165, 180, {"type": "bus"}),
                  (165, 191, {"type": "bus"}),
                  (166, 181, {"type": "taxi"}),
                  (166, 183, {"type": "taxi"}),
                  (167, 168, {"type": "taxi"}),
                  (167, 183, {"type": "taxi"}),
                  (168, 184, {"type": "taxi"}),
                  (169, 184, {"type": "taxi"}),
                  (170, 185, {"type": "taxi"}),
                  (171, 173, {"type": "taxi"}),
                  (171, 175, {"type": "taxi"}),
                  (171, 199, {"type": "taxi"}),
                  (172, 187, {"type": "taxi"}),
                  (173, 188, {"type": "taxi"}),
                  (174, 175, {"type": "taxi"}),
                  (176, 177, {"type": "taxi"}),
                  (176, 189, {"type": "taxi"}),
                  (176, 190, {"type": "bus"}),
                  (178, 189, {"type": "taxi"}),
                  (178, 191, {"type": "taxi"}),
                  (179, 191, {"type": "taxi"}),
                  (180, 181, {"type": "taxi"}),
                  (180, 184, {"type": "bus"}),
                  (180, 190, {"type": "bus"}),
                  (180, 193, {"type": "taxi"}),
                  (181, 182, {"type": "taxi"}),
                  (181, 193, {"type": "taxi"}),
                  (182, 183, {"type": "taxi"}),
                  (182, 195, {"type": "taxi"}),
                  (183, 196, {"type": "taxi"}),
                  (184, 185, {"type": "taxi"}),
                  (184, 185, {"type": "bus"}),
                  (184, 196, {"type": "taxi"}),
                  (184, 197, {"type": "taxi"}),
                  (185, 186, {"type": "taxi"}),
                  (185, 187, {"type": "bus"}),
                  (186, 198, {"type": "taxi"}),
                  (187, 188, {"type": "taxi"}),
                  (187, 198, {"type": "taxi"}),
                  (188, 199, {"type": "taxi"}),
                  (189, 190, {"type": "taxi"}),
                  (190, 191, {"type": "taxi"}),
                  (190, 191, {"type": "bus"}),
                  (190, 192, {"type": "taxi"}),
                  (191, 192, {"type": "taxi"}),
                  (192, 194, {"type": "taxi"}),
                  (194, 195, {"type": "taxi"}),
                  (195, 197, {"type": "taxi"}),
                  (196, 197, {"type": "taxi"}),
                  (198, 199, {"type": "taxi"})]