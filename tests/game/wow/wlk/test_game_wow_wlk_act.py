# -*- coding: utf-8 -*-

import multibox.game.wow.wlk.act.api as act


def test():
    _ = act.Movement
    _ = act.PetAction
    _ = act.Target
    _ = act.target_leader_key_mapper
    _ = act.Camera
    _ = act.System
    _ = act.General
    _ = act.Warrior
    _ = act.WarriorArm
    _ = act.WarriorFury
    _ = act.WarriorProtection
    _ = act.Paladin
    _ = act.PaladinRetribution
    _ = act.PaladinProtection
    _ = act.PaladinHoly
    _ = act.DK
    _ = act.DKBlood
    _ = act.DKFrost
    _ = act.DKUnholy
    _ = act.Shaman
    _ = act.ShamanElementalCombat
    _ = act.ShamanEnhancement
    _ = act.ShamanRestoration
    _ = act.Hunter
    _ = act.HunterBeastMastery
    _ = act.HunterMarksmanship
    _ = act.HunterSurvival
    _ = act.Druid
    _ = act.DruidBalance
    _ = act.DruidRestoration
    _ = act.DruidFeral
    _ = act.Warlock
    _ = act.WarlockAffliction
    _ = act.WarlockDemonology
    _ = act.WarlockDestruction
    _ = act.Mage
    _ = act.MageArcane
    _ = act.MageFire
    _ = act.MageFrost
    _ = act.Priest
    _ = act.PriestDiscipline
    _ = act.PriestHoly
    _ = act.PriestShadow

    _ = act.PaladinHoly.Beacon_of_Light


if __name__ == "__main__":
    from multibox.tests import run_cov_test

    run_cov_test(__file__, "multibox.game.wow.wlk.act", preview=False)
