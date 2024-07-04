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


acc_fact = AccountFactory()


class CharacterFactory: # pragma: no cover

    @property
    def ra_paladin_pve_protect(self) -> Character:
        return ds.get_character("ra_paladin_pve_protect")

    @property
    def rb_shaman_pve_elemental(self) -> Character:
        return ds.get_character("rb_shaman_pve_elemental")

    @property
    def rc_druid_pve_balance(self) -> Character:
        return ds.get_character("rc_druid_pve_balance")

    @property
    def rd_mage_pve_arcane(self) -> Character:
        return ds.get_character("rd_mage_pve_arcane")

    @property
    def re_priest_pve_shadow(self) -> Character:
        return ds.get_character("re_priest_pve_shadow")

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
    def rj_dk_pve_blood_tank_leader2(self) -> Character:
        return ds.get_character("rj_dk_pve_blood_tank_leader2")

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
    def re_priest_pve_holy(self) -> Character:
        return ds.get_character("re_priest_pve_holy")

    @property
    def re_priest_pve_shadow_5p_team2(self) -> Character:
        return ds.get_character("re_priest_pve_shadow_5p_team2")

    @property
    def rh_druid_pve_resto_5p_team1(self) -> Character:
        return ds.get_character("rh_druid_pve_resto_5p_team1")

    @property
    def ri_paladin_pve_holy_5p_team2(self) -> Character:
        return ds.get_character("ri_paladin_pve_holy_5p_team2")

    @property
    def rj_dk_pve_blood_tank_leader1(self) -> Character:
        return ds.get_character("rj_dk_pve_blood_tank_leader1")

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


char_fact = CharacterFactory()


class CharacterGroupFactory: # pragma: no cover

    @property
    def r_1_to_5(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_5")

    @property
    def r_1_to_10(self) -> OrderedSet[Character]:
        return ds.get_build_group("r_1_to_10")

    @property
    def s_1_to_5(self) -> OrderedSet[Character]:
        return ds.get_build_group("s_1_to_5")


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
    def alliance_r_abcde_solo_dungeon(self) -> Mode:
        return ds.get_mode("alliance_r_abcde_solo_dungeon", Mode)

    @property
    def alliance_r_abcdefghij_solo_raid(self) -> Mode:
        return ds.get_mode("alliance_r_abcdefghij_solo_raid", Mode)

    @property
    def horde_s_abcde_solo_dungeon(self) -> Mode:
        return ds.get_mode("horde_s_abcde_solo_dungeon", Mode)


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
    print(char_fact.ra_paladin_pve_protect)
    print(char_fact.rb_shaman_pve_elemental)
    print(char_fact.rc_druid_pve_balance)
    print(char_fact.rd_mage_pve_arcane)
    print(char_fact.re_priest_pve_shadow)
    print(char_fact.rf_warlock_pve_demonology)
    print(char_fact.rg_hunter_pve_marksman)
    print(char_fact.rh_druid_pve_resto)
    print(char_fact.ri_paladin_pve_holy)
    print(char_fact.rj_dk_pve_blood_tank_leader2)
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
    print(char_fact.re_priest_pve_holy)
    print(char_fact.re_priest_pve_shadow_5p_team2)
    print(char_fact.rh_druid_pve_resto_5p_team1)
    print(char_fact.ri_paladin_pve_holy_5p_team2)
    print(char_fact.rj_dk_pve_blood_tank_leader1)
    print(char_fact.sa_paladin_pve_protect)
    print(char_fact.sb_shaman_pve_elemental)
    print(char_fact.sc_shaman_pve_elemental)
    print(char_fact.sd_shaman_pve_elemental)
    print(char_fact.se_shaman_pve_resto)
    print(char_group_fact.r_1_to_5)
    print(char_group_fact.r_1_to_10)
    print(char_group_fact.s_1_to_5)
    print(client_fact.zhTW_1920_1080)
    print(client_fact.zhTW_1600_900)
    print(client_fact.zhTW_1176_664)
    print(client_fact.zhCN_1920_1080)
    print(client_fact.zhCN_1600_900)
    print(client_fact.zhCN_1176_664)
    print(client_fact.enUS_1920_1080)
    print(client_fact.enUS_1600_900)
    print(client_fact.enUS_1176_664)
    print(mode_fact.alliance_r_abcde_solo_dungeon)
    print(mode_fact.alliance_r_abcdefghij_solo_raid)
    print(mode_fact.horde_s_abcde_solo_dungeon)
# fmt: on