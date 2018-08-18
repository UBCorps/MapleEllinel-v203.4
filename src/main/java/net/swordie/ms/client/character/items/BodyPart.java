package net.swordie.ms.client.character.items;

import java.util.Arrays;

/**
 * Created on 1/7/2018.
 */
public enum BodyPart {
    BP_BASE(0),
    HAIR(0),
    CAP(1),
    FACEACC(2),
    EYEACC(3),
    EARACC(4),
    CLOTHES(5), // Includes overall
    PANTS(6),
    SHOES(7),
    GLOVES(8),
    CAPE(9),
    SHIELD(10), // Includes things such as katara, 2ndary
    WEAPON(11),
    RING1(12),
    RING2(13),
    PETWEAR(14),
    RING3(15),
    RING4(16),
    PENDANT(17),
    TAMINGMOB(18),
    SADDLE(19),
    MOBEQUIP(20),
    MEDAL_OLD(21), // ?
    BELT(22),
    SHOULDER(23),
    PETWEAR2(24),
    PETWEAR3(25),
    CHARMACC(26),
    ANDROID(27),
    MACHINEHEART(28),
    BADGE(29),
    EMBLEM(30),
    EXT_0(31),
    EXT_PENDANT1(31),
    EXT_1(32),
    EXT_2(33),
    EXT_3(34),
    EXT_4(35),
    EXT_5(36),
    EXT_6(37),
    MEDAL(49), // ?
    BOOK(55),
    STICKER(100),
    BP_END(100),
    CBP_BASE(101), // CASH
    PET_CONSUME_HP_ITEM(200),
    PET_CONSUME_MP_ITEM(201),
    CBP_END(1000),
    EVAN_BASE(1000),
    EVAN_CAP(1000),
    EVAN_PENDANT(1001),
    EVAN_WING(1002),
    EVAN_SHOES(1003),
    EVAN_END(1004),
    MECH_BASE(1100),
    MECH_ENGINE(1100),
    MECH_ARM(1101),
    MECH_LEG(1102),
    MECH_FRAME(1103),
    MECH_TRANSISTOR(1104),
    MECH_END(1105),
    AP_BASE(1200),
    AP_CAP(1200),
    AP_CAPE(1201),
    AP_FACEACC(1203),
    AP_CLOTHES(1204),
    AP_PANTS(1204),
    AP_SHOES(1205),
    AP_GLOVES(1206),
    AP_END(1207),
    DU_BASE(1300),
    DU_CAP(1300),
    DU_CAPE(1301),
    DU_FACEACC(1302),
    DU_CLOTHES(1303),
    DU_GLOVES(1304),
    DU_END(1305),
    BITS_BASE(1400), // 1400~1424
    BITS_END(1425),
    ZERO_BASE(1500),
    ZERO_EYEACC(1500),
    ZERO_CAP(1501),
    ZERO_FACEACC(1502),
    ZERO_EARACC(1503),
    ZERO_CAPE(1504),
    ZERO_CLOTHES(1505),
    ZERO_GLOVES(1506),
    ZERO_WEAPON(1507),
    ZERO_PANTS(1508),
    ZERO_SHOES(1509),
    ZERO_RING1(1510),
    ZERO_RING2(1511),
    ZERO_END(1512),
    TOTEM_BASE(5000),
    TOTEM1(5000),
    TOTEM2(5001),
    TOTEM3(5002),
    TOTEM4(5003),
    TOTEM_END(5004),
    MBP_BASE(5100),
    MBP_CAP(5101),
    MBP_CAPE(5102),
    MBP_CLOTHES(5103),
    MBP_GLOVES(5104),
    MBP_SHOES(5105),
    MBP_WEAPON(5106),
    MBP_END(5107),
    FP_START(5200),
    FP_WEAPON(5200),
    FP_END(5201),
    SLOT_INDEX_NOT_DEFINED(15440),;

    private int val;

    BodyPart(int val) {
        this.val = val;
    }

    public static BodyPart getByVal(int bodyPartVal) {
        return Arrays.stream(values()).filter(bp -> bp.getVal() == bodyPartVal).findAny().orElse(null);
    }

    public int getVal() {
        return val;
    }
}
