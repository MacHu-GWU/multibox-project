# -*- coding: utf-8 -*-

from ordered_set import OrderedSet

from multibox.game.wow.wlk.api import (
    Character,
    Client,
)

from gen_dataset import ds

# fmt: off
class AccountFactory:
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


acc_fact = AccountFactory()


class CharacterFactory:
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
    def rj_dk_pve_blood_tank(self) -> Character:
        return ds.get_character("rj_dk_pve_blood_tank")


char_fact = CharacterFactory()


class CharacterGroupFactory:
    @property
    def all(self) -> OrderedSet[Character]:
        return ds.get_build_group("all")


char_group_fact = CharacterGroupFactory()


class ClientFactory:
    @property
    def c_1920_1080(self) -> Client:
        return ds.get_client("c_1920_1080")
    @property
    def c_1600_900(self) -> Client:
        return ds.get_client("c_1600_900")
    @property
    def c_1176_664(self) -> Client:
        return ds.get_client("c_1176_664")


client_fact = ClientFactory()


if __name__ == "__main__":
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
    print(char_fact.ra_paladin_pve_protect)
    print(char_fact.rb_shaman_pve_elemental)
    print(char_fact.rc_druid_pve_balance)
    print(char_fact.rd_mage_pve_arcane)
    print(char_fact.re_priest_pve_shadow)
    print(char_fact.rf_warlock_pve_demonology)
    print(char_fact.rg_hunter_pve_marksman)
    print(char_fact.rh_druid_pve_resto)
    print(char_fact.ri_paladin_pve_holy)
    print(char_fact.rj_dk_pve_blood_tank)
    print(char_group_fact.all)
    print(client_fact.c_1920_1080)
    print(client_fact.c_1600_900)
    print(client_fact.c_1176_664)
# fmt: on