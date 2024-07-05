# -*- coding: utf-8 -*-

from ordered_set import OrderedSet

from multibox.game.wow.wlk.api import (
    Character,
    Client,
)
from multibox.game.wow.wlk.preset.my_mode.api import Mode
try:
    from .gen_dataset import ds
except ImportError: # pragma: no cover
    from gen_dataset import ds



# fmt: off
class AccountFactory: # pragma: no cover
    Fat01 = ds.get_account("Fat01")
    Fat02 = ds.get_account("Fat02")
    Fat03 = ds.get_account("Fat03")
    Fat04 = ds.get_account("Fat04")
    Fat05 = ds.get_account("Fat05")
    Fat06 = ds.get_account("Fat06")
    Fat07 = ds.get_account("Fat07")
    Fat08 = ds.get_account("Fat08")
    Fat09 = ds.get_account("Fat09")
    Fat10 = ds.get_account("Fat10")
    Fat11 = ds.get_account("Fat11")
    Fat12 = ds.get_account("Fat12")
    Fat13 = ds.get_account("Fat13")
    Fat14 = ds.get_account("Fat14")
    Fat15 = ds.get_account("Fat15")
    Fat16 = ds.get_account("Fat16")
    Fat17 = ds.get_account("Fat17")
    Fat18 = ds.get_account("Fat18")
    Fat19 = ds.get_account("Fat19")
    Fat20 = ds.get_account("Fat20")
    Fat21 = ds.get_account("Fat21")
    Fat22 = ds.get_account("Fat22")
    Fat23 = ds.get_account("Fat23")
    Fat24 = ds.get_account("Fat24")
    Fat25 = ds.get_account("Fat25")
    Rab01 = ds.get_account("Rab01")
    Rab02 = ds.get_account("Rab02")
    Rab03 = ds.get_account("Rab03")
    Rab04 = ds.get_account("Rab04")
    Rab05 = ds.get_account("Rab05")
    Fatmulti1 = ds.get_account("Fatmulti1")
    Fatmulti2 = ds.get_account("Fatmulti2")
    Fatmulti3 = ds.get_account("Fatmulti3")
    Fatmulti4 = ds.get_account("Fatmulti4")
    Fatmulti5 = ds.get_account("Fatmulti5")
    Fitsheep = ds.get_account("Fitsheep")
    Fatmulti6 = ds.get_account("Fatmulti6")
    Fatmulti8 = ds.get_account("Fatmulti8")
    Fatmulti9 = ds.get_account("Fatmulti9")
    Fatmulti10 = ds.get_account("Fatmulti10")
    Fatmulti11 = ds.get_account("Fatmulti11")
    Fatmulti12 = ds.get_account("Fatmulti12")
    Fatmulti13 = ds.get_account("Fatmulti13")
    Fatmulti14 = ds.get_account("Fatmulti14")
    Fatmulti15 = ds.get_account("Fatmulti15")
    Fatmulti16 = ds.get_account("Fatmulti16")
    Fatmulti17 = ds.get_account("Fatmulti17")
    Fatmulti18 = ds.get_account("Fatmulti18")
    Fatmulti19 = ds.get_account("Fatmulti19")
    Fatmulti20 = ds.get_account("Fatmulti20")
    Fatmulti21 = ds.get_account("Fatmulti21")
    Fatmulti22 = ds.get_account("Fatmulti22")
    Fatmulti23 = ds.get_account("Fatmulti23")
    Fatmulti24 = ds.get_account("Fatmulti24")
    Fatmulti25 = ds.get_account("Fatmulti25")
    Fatmulti26 = ds.get_account("Fatmulti26")
    Makun7551 = ds.get_account("Makun7551")


acc_fact = AccountFactory()


class CharacterFactory: # pragma: no cover

    @property
    def ra_paladin_pve_protect(self) -> Character:
        return ds.get_character("ra_paladin_pve_protect")

    @property
    def rb_shaman_pve_elemental(self) -> Character:
        return ds.get_character("rb_shaman_pve_elemental")

    @property
    def rb_shaman_pve_resto(self) -> Character:
        return ds.get_character("rb_shaman_pve_resto")

    @property
    def rc_druid_pve_balance(self) -> Character:
        return ds.get_character("rc_druid_pve_balance")

    @property
    def rc_druid_pve_bear(self) -> Character:
        return ds.get_character("rc_druid_pve_bear")

    @property
    def rd_mage_pve_arcane(self) -> Character:
        return ds.get_character("rd_mage_pve_arcane")

    @property
    def re_priest_pve_shadow(self) -> Character:
        return ds.get_character("re_priest_pve_shadow")

    @property
    def re_priest_pve_holy(self) -> Character:
        return ds.get_character("re_priest_pve_holy")

    @property
    def rf_warlock_pve_demonology(self) -> Character:
        return ds.get_character("rf_warlock_pve_demonology")

    @property
    def rg_hunter_pve_marksman(self) -> Character:
        return ds.get_character("rg_hunter_pve_marksman")

    @property
    def rh_druid_pve_resto(self) -> Character:
        return ds.get_character("rh_druid_pve_resto")

    @property
    def ri_paladin_pve_holy(self) -> Character:
        return ds.get_character("ri_paladin_pve_holy")

    @property
    def rj_dk_pve_blood_tank(self) -> Character:
        return ds.get_character("rj_dk_pve_blood_tank")

    @property
    def rk_druid_pve_balance(self) -> Character:
        return ds.get_character("rk_druid_pve_balance")

    @property
    def rl_druid_pve_balance(self) -> Character:
        return ds.get_character("rl_druid_pve_balance")

    @property
    def rm_druid_pve_balance(self) -> Character:
        return ds.get_character("rm_druid_pve_balance")

    @property
    def rn_priest_pve_shadow(self) -> Character:
        return ds.get_character("rn_priest_pve_shadow")

    @property
    def ro_priest_pve_shadow(self) -> Character:
        return ds.get_character("ro_priest_pve_shadow")

    @property
    def rp_priest_pve_shadow(self) -> Character:
        return ds.get_character("rp_priest_pve_shadow")

    @property
    def rq_priest_pve_shadow(self) -> Character:
        return ds.get_character("rq_priest_pve_shadow")

    @property
    def rr_priest_pve_shadow(self) -> Character:
        return ds.get_character("rr_priest_pve_shadow")

    @property
    def rs_priest_pve_shadow(self) -> Character:
        return ds.get_character("rs_priest_pve_shadow")

    @property
    def rt_priest_pve_shadow(self) -> Character:
        return ds.get_character("rt_priest_pve_shadow")

    @property
    def ru_priest_pve_shadow(self) -> Character:
        return ds.get_character("ru_priest_pve_shadow")

    @property
    def rv_priest_pve_shadow(self) -> Character:
        return ds.get_character("rv_priest_pve_shadow")

    @property
    def rw_shaman_pve_resto(self) -> Character:
        return ds.get_character("rw_shaman_pve_resto")

    @property
    def rx_paladin_pve_holy(self) -> Character:
        return ds.get_character("rx_paladin_pve_holy")

    @property
    def ry_priest_pve_disco(self) -> Character:
        return ds.get_character("ry_priest_pve_disco")

    @property
    def sa_paladin_pve_protect(self) -> Character:
        return ds.get_character("sa_paladin_pve_protect")

    @property
    def sb_shaman_pve_elemental(self) -> Character:
        return ds.get_character("sb_shaman_pve_elemental")

    @property
    def sc_shaman_pve_elemental(self) -> Character:
        return ds.get_character("sc_shaman_pve_elemental")

    @property
    def sd_shaman_pve_elemental(self) -> Character:
        return ds.get_character("sd_shaman_pve_elemental")

    @property
    def se_shaman_pve_resto(self) -> Character:
        return ds.get_character("se_shaman_pve_resto")

    @property
    def batlefury_paladin_pve_protect(self) -> Character:
        return ds.get_character("batlefury_paladin_pve_protect")

    @property
    def batlefury_paladin_pve_retri(self) -> Character:
        return ds.get_character("batlefury_paladin_pve_retri")

    @property
    def litgoatssa_warlock_pve_demonology(self) -> Character:
        return ds.get_character("litgoatssa_warlock_pve_demonology")

    @property
    def litgoatdka_dk_pve_blood_tank(self) -> Character:
        return ds.get_character("litgoatdka_dk_pve_blood_tank")

    @property
    def litgoatdka_dk_pvp_frost(self) -> Character:
        return ds.get_character("litgoatdka_dk_pvp_frost")

    @property
    def quentinquinn_shaman_pve_elemental(self) -> Character:
        return ds.get_character("quentinquinn_shaman_pve_elemental")

    @property
    def quentinquinn_shaman_pve_resto(self) -> Character:
        return ds.get_character("quentinquinn_shaman_pve_resto")

    @property
    def litgoatssb_warlock_pve_demonology(self) -> Character:
        return ds.get_character("litgoatssb_warlock_pve_demonology")

    @property
    def litgoatdkb_dk_pve_unholy_dps(self) -> Character:
        return ds.get_character("litgoatdkb_dk_pve_unholy_dps")

    @property
    def litgoatdkb_dk_pvp_frost(self) -> Character:
        return ds.get_character("litgoatdkb_dk_pvp_frost")

    @property
    def opiitou_druid_pve_balance(self) -> Character:
        return ds.get_character("opiitou_druid_pve_balance")

    @property
    def opiitou_druid_pve_bear(self) -> Character:
        return ds.get_character("opiitou_druid_pve_bear")

    @property
    def litgoatssc_warlock_pve_demonology(self) -> Character:
        return ds.get_character("litgoatssc_warlock_pve_demonology")

    @property
    def litgoatdkc_dk_pve_unholy_dps(self) -> Character:
        return ds.get_character("litgoatdkc_dk_pve_unholy_dps")

    @property
    def litgoatdkc_dk_pvp_frost(self) -> Character:
        return ds.get_character("litgoatdkc_dk_pvp_frost")

    @property
    def swagsonic_mage_pve_arcane(self) -> Character:
        return ds.get_character("swagsonic_mage_pve_arcane")

    @property
    def swagsonic_mage_pve_fire(self) -> Character:
        return ds.get_character("swagsonic_mage_pve_fire")

    @property
    def litgoatssd_warlock_pve_demonology(self) -> Character:
        return ds.get_character("litgoatssd_warlock_pve_demonology")

    @property
    def litgoatdkd_dk_pve_unholy_dps(self) -> Character:
        return ds.get_character("litgoatdkd_dk_pve_unholy_dps")

    @property
    def litgoatdkd_dk_pvp_frost(self) -> Character:
        return ds.get_character("litgoatdkd_dk_pvp_frost")

    @property
    def kangliu_priest_pve_shadow(self) -> Character:
        return ds.get_character("kangliu_priest_pve_shadow")

    @property
    def kangliu_priest_pve_disco(self) -> Character:
        return ds.get_character("kangliu_priest_pve_disco")

    @property
    def litgoatsse_warlock_pve_demonology(self) -> Character:
        return ds.get_character("litgoatsse_warlock_pve_demonology")

    @property
    def litgoatdke_dk_pve_unholy_dps(self) -> Character:
        return ds.get_character("litgoatdke_dk_pve_unholy_dps")

    @property
    def litgoatdke_dk_pvp_frost(self) -> Character:
        return ds.get_character("litgoatdke_dk_pvp_frost")

    @property
    def kindhearted_warlock_pve_demonology(self) -> Character:
        return ds.get_character("kindhearted_warlock_pve_demonology")

    @property
    def kindhearted_warlock_pve_destruction(self) -> Character:
        return ds.get_character("kindhearted_warlock_pve_destruction")

    @property
    def bordercollie_priest_pve_disco(self) -> Character:
        return ds.get_character("bordercollie_priest_pve_disco")

    @property
    def bordercollie_priest_pve_shadow(self) -> Character:
        return ds.get_character("bordercollie_priest_pve_shadow")

    @property
    def sweetmonk_warrior_pve_fury(self) -> Character:
        return ds.get_character("sweetmonk_warrior_pve_fury")

    @property
    def sweetmonk_warrior_pve_protect(self) -> Character:
        return ds.get_character("sweetmonk_warrior_pve_protect")

    @property
    def kapacuk_hunter_pve_marksman(self) -> Character:
        return ds.get_character("kapacuk_hunter_pve_marksman")

    @property
    def healthymonk_paladin_pve_holy(self) -> Character:
        return ds.get_character("healthymonk_paladin_pve_holy")

    @property
    def bunnysisters_druid_pve_resto(self) -> Character:
        return ds.get_character("bunnysisters_druid_pve_resto")

    @property
    def bunnysisters_druid_pve_balance(self) -> Character:
        return ds.get_character("bunnysisters_druid_pve_balance")

    @property
    def honeymonk_shaman_pve_enhancement(self) -> Character:
        return ds.get_character("honeymonk_shaman_pve_enhancement")

    @property
    def glowyy_paladin_pve_holy(self) -> Character:
        return ds.get_character("glowyy_paladin_pve_holy")

    @property
    def glowyy_paladin_pve_protect(self) -> Character:
        return ds.get_character("glowyy_paladin_pve_protect")

    @property
    def chubbymonk_druid_pve_balance(self) -> Character:
        return ds.get_character("chubbymonk_druid_pve_balance")

    @property
    def luxiaofeng_dk_pve_unholy_tank(self) -> Character:
        return ds.get_character("luxiaofeng_dk_pve_unholy_tank")

    @property
    def luxiaofeng_dk_pve_blood_tank(self) -> Character:
        return ds.get_character("luxiaofeng_dk_pve_blood_tank")

    @property
    def shinymonk_priest_pve_shadow(self) -> Character:
        return ds.get_character("shinymonk_priest_pve_shadow")

    @property
    def litgugua_druid_pve_balance(self) -> Character:
        return ds.get_character("litgugua_druid_pve_balance")

    @property
    def litgugua_druid_pve_resto(self) -> Character:
        return ds.get_character("litgugua_druid_pve_resto")

    @property
    def litgugub_druid_pve_balance(self) -> Character:
        return ds.get_character("litgugub_druid_pve_balance")

    @property
    def litgugub_druid_pve_resto(self) -> Character:
        return ds.get_character("litgugub_druid_pve_resto")

    @property
    def litguguc_druid_pve_balance(self) -> Character:
        return ds.get_character("litguguc_druid_pve_balance")

    @property
    def litguguc_druid_pve_resto(self) -> Character:
        return ds.get_character("litguguc_druid_pve_resto")

    @property
    def litgugud_druid_pve_balance(self) -> Character:
        return ds.get_character("litgugud_druid_pve_balance")

    @property
    def litgugud_druid_pve_resto(self) -> Character:
        return ds.get_character("litgugud_druid_pve_resto")

    @property
    def litgugue_druid_pvp_balance(self) -> Character:
        return ds.get_character("litgugue_druid_pvp_balance")

    @property
    def litgugue_druid_pvp_resto(self) -> Character:
        return ds.get_character("litgugue_druid_pvp_resto")

    @property
    def litguguf_druid_pvp_balance(self) -> Character:
        return ds.get_character("litguguf_druid_pvp_balance")

    @property
    def litguguf_druid_pvp_resto(self) -> Character:
        return ds.get_character("litguguf_druid_pvp_resto")

    @property
    def litgugug_druid_pvp_balance(self) -> Character:
        return ds.get_character("litgugug_druid_pvp_balance")

    @property
    def litgugug_druid_pvp_resto(self) -> Character:
        return ds.get_character("litgugug_druid_pvp_resto")

    @property
    def litguguh_druid_pvp_balance(self) -> Character:
        return ds.get_character("litguguh_druid_pvp_balance")

    @property
    def litguguh_druid_pvp_resto(self) -> Character:
        return ds.get_character("litguguh_druid_pvp_resto")

    @property
    def lgmsi_priest_pve_shadow(self) -> Character:
        return ds.get_character("lgmsi_priest_pve_shadow")

    @property
    def lgmsi_priest_pve_disco(self) -> Character:
        return ds.get_character("lgmsi_priest_pve_disco")

    @property
    def lgmsj_priest_pve_shadow(self) -> Character:
        return ds.get_character("lgmsj_priest_pve_shadow")

    @property
    def lgmsj_priest_pve_disco(self) -> Character:
        return ds.get_character("lgmsj_priest_pve_disco")

    @property
    def lgmsk_priest_pve_shadow(self) -> Character:
        return ds.get_character("lgmsk_priest_pve_shadow")

    @property
    def lgmsk_priest_pve_disco(self) -> Character:
        return ds.get_character("lgmsk_priest_pve_disco")

    @property
    def lgmsl_priest_pve_shadow(self) -> Character:
        return ds.get_character("lgmsl_priest_pve_shadow")

    @property
    def lgmsl_priest_pve_disco(self) -> Character:
        return ds.get_character("lgmsl_priest_pve_disco")

    @property
    def lgsmm_shaman_pve_elemental(self) -> Character:
        return ds.get_character("lgsmm_shaman_pve_elemental")

    @property
    def lgsmm_shaman_pve_resto(self) -> Character:
        return ds.get_character("lgsmm_shaman_pve_resto")

    @property
    def lgsmn_shaman_pve_elemental(self) -> Character:
        return ds.get_character("lgsmn_shaman_pve_elemental")

    @property
    def lgsmn_shaman_pve_resto(self) -> Character:
        return ds.get_character("lgsmn_shaman_pve_resto")

    @property
    def lgsmo_shaman_pve_elemental(self) -> Character:
        return ds.get_character("lgsmo_shaman_pve_elemental")

    @property
    def lgsmo_shaman_pve_resto(self) -> Character:
        return ds.get_character("lgsmo_shaman_pve_resto")

    @property
    def lgsmp_shaman_pve_elemental(self) -> Character:
        return ds.get_character("lgsmp_shaman_pve_elemental")

    @property
    def lgsmp_shaman_pve_resto(self) -> Character:
        return ds.get_character("lgsmp_shaman_pve_resto")

    @property
    def laoshou_paladin_pve_protect(self) -> Character:
        return ds.get_character("laoshou_paladin_pve_protect")

    @property
    def laoshou_paladin_pve_retri(self) -> Character:
        return ds.get_character("laoshou_paladin_pve_retri")

    @property
    def ganjj_dk_pve_blood_tank(self) -> Character:
        return ds.get_character("ganjj_dk_pve_blood_tank")

    @property
    def ganjj_dk_pve_unholy_tank(self) -> Character:
        return ds.get_character("ganjj_dk_pve_unholy_tank")


char_fact = CharacterFactory()


class CharacterGroupFactory: # pragma: no cover

    @property
    def r_1_to_5(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_5")

    @property
    def r_1_to_10(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_10")

    @property
    def r_1_to_10_solo_dungeon_team1(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_10_solo_dungeon_team1")

    @property
    def r_1_to_10_solo_icc_boss1(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_10_solo_icc_boss1")

    @property
    def r_1_to_10_solo_dungeon_team2(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_10_solo_dungeon_team2")

    @property
    def s_1_to_5(self) -> OrderedSet[Character]:
        return ds.get_build_group("s_1_to_5")

    @property
    def warmane_quarterly_login_team1(self) -> OrderedSet[Character]:
        return ds.get_build_group("warmane_quarterly_login_team1")

    @property
    def warmane_quarterly_login_team2(self) -> OrderedSet[Character]:
        return ds.get_build_group("warmane_quarterly_login_team2")


char_group_fact = CharacterGroupFactory()


class ClientFactory: # pragma: no cover

    @property
    def zhTW_1920_1080(self) -> Client:
        return ds.get_client("zhTW_1920_1080")

    @property
    def zhTW_1600_900(self) -> Client:
        return ds.get_client("zhTW_1600_900")

    @property
    def zhTW_1176_664(self) -> Client:
        return ds.get_client("zhTW_1176_664")

    @property
    def zhCN_1920_1080(self) -> Client:
        return ds.get_client("zhCN_1920_1080")

    @property
    def zhCN_1600_900(self) -> Client:
        return ds.get_client("zhCN_1600_900")

    @property
    def zhCN_1176_664(self) -> Client:
        return ds.get_client("zhCN_1176_664")

    @property
    def enUS_1920_1080(self) -> Client:
        return ds.get_client("enUS_1920_1080")

    @property
    def enUS_1600_900(self) -> Client:
        return ds.get_client("enUS_1600_900")

    @property
    def enUS_1176_664(self) -> Client:
        return ds.get_client("enUS_1176_664")


client_fact = ClientFactory()


class ModeFactory: # pragma: no cover

    @property
    def acore_alliance_r_abcde_solo_dungeon(self) -> Mode:
        return ds.get_mode("acore_alliance_r_abcde_solo_dungeon", Mode)

    @property
    def acore_alliance_r_abcdefghij_solo_raid(self) -> Mode:
        return ds.get_mode("acore_alliance_r_abcdefghij_solo_raid", Mode)

    @property
    def acore_alliance_r_abcdefghij_solo_icc_boss1(self) -> Mode:
        return ds.get_mode("acore_alliance_r_abcdefghij_solo_icc_boss1", Mode)

    @property
    def acore_horde_s_abcde_solo_dungeon(self) -> Mode:
        return ds.get_mode("acore_horde_s_abcde_solo_dungeon", Mode)

    @property
    def warmane_quarterly_login_team1(self) -> Mode:
        return ds.get_mode("warmane_quarterly_login_team1", Mode)

    @property
    def warmane_quarterly_login_team2(self) -> Mode:
        return ds.get_mode("warmane_quarterly_login_team2", Mode)


mode_fact = ModeFactory()


if __name__ == "__main__": # pragma: no cover
    # You can run this script as "main" to test it
    print(acc_fact.Fat01)
    print(acc_fact.Fat02)
    print(acc_fact.Fat03)
    print(acc_fact.Fat04)
    print(acc_fact.Fat05)
    print(acc_fact.Fat06)
    print(acc_fact.Fat07)
    print(acc_fact.Fat08)
    print(acc_fact.Fat09)
    print(acc_fact.Fat10)
    print(acc_fact.Fat11)
    print(acc_fact.Fat12)
    print(acc_fact.Fat13)
    print(acc_fact.Fat14)
    print(acc_fact.Fat15)
    print(acc_fact.Fat16)
    print(acc_fact.Fat17)
    print(acc_fact.Fat18)
    print(acc_fact.Fat19)
    print(acc_fact.Fat20)
    print(acc_fact.Fat21)
    print(acc_fact.Fat22)
    print(acc_fact.Fat23)
    print(acc_fact.Fat24)
    print(acc_fact.Fat25)
    print(acc_fact.Rab01)
    print(acc_fact.Rab02)
    print(acc_fact.Rab03)
    print(acc_fact.Rab04)
    print(acc_fact.Rab05)
    print(acc_fact.Fatmulti1)
    print(acc_fact.Fatmulti2)
    print(acc_fact.Fatmulti3)
    print(acc_fact.Fatmulti4)
    print(acc_fact.Fatmulti5)
    print(acc_fact.Fitsheep)
    print(acc_fact.Fatmulti6)
    print(acc_fact.Fatmulti8)
    print(acc_fact.Fatmulti9)
    print(acc_fact.Fatmulti10)
    print(acc_fact.Fatmulti11)
    print(acc_fact.Fatmulti12)
    print(acc_fact.Fatmulti13)
    print(acc_fact.Fatmulti14)
    print(acc_fact.Fatmulti15)
    print(acc_fact.Fatmulti16)
    print(acc_fact.Fatmulti17)
    print(acc_fact.Fatmulti18)
    print(acc_fact.Fatmulti19)
    print(acc_fact.Fatmulti20)
    print(acc_fact.Fatmulti21)
    print(acc_fact.Fatmulti22)
    print(acc_fact.Fatmulti23)
    print(acc_fact.Fatmulti24)
    print(acc_fact.Fatmulti25)
    print(acc_fact.Fatmulti26)
    print(acc_fact.Makun7551)
    print(char_fact.ra_paladin_pve_protect)
    print(char_fact.rb_shaman_pve_elemental)
    print(char_fact.rb_shaman_pve_resto)
    print(char_fact.rc_druid_pve_balance)
    print(char_fact.rc_druid_pve_bear)
    print(char_fact.rd_mage_pve_arcane)
    print(char_fact.re_priest_pve_shadow)
    print(char_fact.re_priest_pve_holy)
    print(char_fact.rf_warlock_pve_demonology)
    print(char_fact.rg_hunter_pve_marksman)
    print(char_fact.rh_druid_pve_resto)
    print(char_fact.ri_paladin_pve_holy)
    print(char_fact.rj_dk_pve_blood_tank)
    print(char_fact.rk_druid_pve_balance)
    print(char_fact.rl_druid_pve_balance)
    print(char_fact.rm_druid_pve_balance)
    print(char_fact.rn_priest_pve_shadow)
    print(char_fact.ro_priest_pve_shadow)
    print(char_fact.rp_priest_pve_shadow)
    print(char_fact.rq_priest_pve_shadow)
    print(char_fact.rr_priest_pve_shadow)
    print(char_fact.rs_priest_pve_shadow)
    print(char_fact.rt_priest_pve_shadow)
    print(char_fact.ru_priest_pve_shadow)
    print(char_fact.rv_priest_pve_shadow)
    print(char_fact.rw_shaman_pve_resto)
    print(char_fact.rx_paladin_pve_holy)
    print(char_fact.ry_priest_pve_disco)
    print(char_fact.sa_paladin_pve_protect)
    print(char_fact.sb_shaman_pve_elemental)
    print(char_fact.sc_shaman_pve_elemental)
    print(char_fact.sd_shaman_pve_elemental)
    print(char_fact.se_shaman_pve_resto)
    print(char_fact.batlefury_paladin_pve_protect)
    print(char_fact.batlefury_paladin_pve_retri)
    print(char_fact.litgoatssa_warlock_pve_demonology)
    print(char_fact.litgoatdka_dk_pve_blood_tank)
    print(char_fact.litgoatdka_dk_pvp_frost)
    print(char_fact.quentinquinn_shaman_pve_elemental)
    print(char_fact.quentinquinn_shaman_pve_resto)
    print(char_fact.litgoatssb_warlock_pve_demonology)
    print(char_fact.litgoatdkb_dk_pve_unholy_dps)
    print(char_fact.litgoatdkb_dk_pvp_frost)
    print(char_fact.opiitou_druid_pve_balance)
    print(char_fact.opiitou_druid_pve_bear)
    print(char_fact.litgoatssc_warlock_pve_demonology)
    print(char_fact.litgoatdkc_dk_pve_unholy_dps)
    print(char_fact.litgoatdkc_dk_pvp_frost)
    print(char_fact.swagsonic_mage_pve_arcane)
    print(char_fact.swagsonic_mage_pve_fire)
    print(char_fact.litgoatssd_warlock_pve_demonology)
    print(char_fact.litgoatdkd_dk_pve_unholy_dps)
    print(char_fact.litgoatdkd_dk_pvp_frost)
    print(char_fact.kangliu_priest_pve_shadow)
    print(char_fact.kangliu_priest_pve_disco)
    print(char_fact.litgoatsse_warlock_pve_demonology)
    print(char_fact.litgoatdke_dk_pve_unholy_dps)
    print(char_fact.litgoatdke_dk_pvp_frost)
    print(char_fact.kindhearted_warlock_pve_demonology)
    print(char_fact.kindhearted_warlock_pve_destruction)
    print(char_fact.bordercollie_priest_pve_disco)
    print(char_fact.bordercollie_priest_pve_shadow)
    print(char_fact.sweetmonk_warrior_pve_fury)
    print(char_fact.sweetmonk_warrior_pve_protect)
    print(char_fact.kapacuk_hunter_pve_marksman)
    print(char_fact.healthymonk_paladin_pve_holy)
    print(char_fact.bunnysisters_druid_pve_resto)
    print(char_fact.bunnysisters_druid_pve_balance)
    print(char_fact.honeymonk_shaman_pve_enhancement)
    print(char_fact.glowyy_paladin_pve_holy)
    print(char_fact.glowyy_paladin_pve_protect)
    print(char_fact.chubbymonk_druid_pve_balance)
    print(char_fact.luxiaofeng_dk_pve_unholy_tank)
    print(char_fact.luxiaofeng_dk_pve_blood_tank)
    print(char_fact.shinymonk_priest_pve_shadow)
    print(char_fact.litgugua_druid_pve_balance)
    print(char_fact.litgugua_druid_pve_resto)
    print(char_fact.litgugub_druid_pve_balance)
    print(char_fact.litgugub_druid_pve_resto)
    print(char_fact.litguguc_druid_pve_balance)
    print(char_fact.litguguc_druid_pve_resto)
    print(char_fact.litgugud_druid_pve_balance)
    print(char_fact.litgugud_druid_pve_resto)
    print(char_fact.litgugue_druid_pvp_balance)
    print(char_fact.litgugue_druid_pvp_resto)
    print(char_fact.litguguf_druid_pvp_balance)
    print(char_fact.litguguf_druid_pvp_resto)
    print(char_fact.litgugug_druid_pvp_balance)
    print(char_fact.litgugug_druid_pvp_resto)
    print(char_fact.litguguh_druid_pvp_balance)
    print(char_fact.litguguh_druid_pvp_resto)
    print(char_fact.lgmsi_priest_pve_shadow)
    print(char_fact.lgmsi_priest_pve_disco)
    print(char_fact.lgmsj_priest_pve_shadow)
    print(char_fact.lgmsj_priest_pve_disco)
    print(char_fact.lgmsk_priest_pve_shadow)
    print(char_fact.lgmsk_priest_pve_disco)
    print(char_fact.lgmsl_priest_pve_shadow)
    print(char_fact.lgmsl_priest_pve_disco)
    print(char_fact.lgsmm_shaman_pve_elemental)
    print(char_fact.lgsmm_shaman_pve_resto)
    print(char_fact.lgsmn_shaman_pve_elemental)
    print(char_fact.lgsmn_shaman_pve_resto)
    print(char_fact.lgsmo_shaman_pve_elemental)
    print(char_fact.lgsmo_shaman_pve_resto)
    print(char_fact.lgsmp_shaman_pve_elemental)
    print(char_fact.lgsmp_shaman_pve_resto)
    print(char_fact.laoshou_paladin_pve_protect)
    print(char_fact.laoshou_paladin_pve_retri)
    print(char_fact.ganjj_dk_pve_blood_tank)
    print(char_fact.ganjj_dk_pve_unholy_tank)
    print(char_group_fact.r_1_to_5)
    print(char_group_fact.r_1_to_10)
    print(char_group_fact.r_1_to_10_solo_dungeon_team1)
    print(char_group_fact.r_1_to_10_solo_icc_boss1)
    print(char_group_fact.r_1_to_10_solo_dungeon_team2)
    print(char_group_fact.s_1_to_5)
    print(char_group_fact.warmane_quarterly_login_team1)
    print(char_group_fact.warmane_quarterly_login_team2)
    print(client_fact.zhTW_1920_1080)
    print(client_fact.zhTW_1600_900)
    print(client_fact.zhTW_1176_664)
    print(client_fact.zhCN_1920_1080)
    print(client_fact.zhCN_1600_900)
    print(client_fact.zhCN_1176_664)
    print(client_fact.enUS_1920_1080)
    print(client_fact.enUS_1600_900)
    print(client_fact.enUS_1176_664)
    print(mode_fact.acore_alliance_r_abcde_solo_dungeon)
    print(mode_fact.acore_alliance_r_abcdefghij_solo_raid)
    print(mode_fact.acore_alliance_r_abcdefghij_solo_icc_boss1)
    print(mode_fact.acore_horde_s_abcde_solo_dungeon)
    print(mode_fact.warmane_quarterly_login_team1)
    print(mode_fact.warmane_quarterly_login_team2)
# fmt: on