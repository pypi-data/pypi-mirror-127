# -*- coding: utf-8 -*-

#  Copyright (c) 2021, University of Luxembourg / DHARPA project
#  Copyright (c) 2021, Markus Binsteiner
#
#  Mozilla Public License, version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

from click.testing import CliRunner

from kiara import Kiara
from kiara.interfaces.cli import cli


def test_data_subcommand():

    runner = CliRunner()
    result = runner.invoke(cli, "data")
    assert result.exit_code == 0
    assert "Print the metadata" in result.stdout


def test_data_list_subcommand(presseeded_data_store_minimal: Kiara):

    runner = CliRunner()
    result = runner.invoke(
        cli,
        "data list --all",
        env={"KIARA_DATA_STORE": presseeded_data_store_minimal.config.data_store},
    )

    assert result.exit_code == 0
    # assert "journal_nodes_table" in result.stdout
    assert "journal_nodes@1" in result.stdout


def test_data_load_subcommand(presseeded_data_store_minimal: Kiara):

    runner = CliRunner()
    result = runner.invoke(
        cli,
        "data load journal_nodes",
        env={"KIARA_DATA_STORE": presseeded_data_store_minimal.config.data_store},
    )

    # assert "Psychiatrische en neurologische bladen" in result.stdout
    assert "City" in result.stdout


def test_data_explain_subcommand(presseeded_data_store_minimal: Kiara):

    runner = CliRunner()
    result = runner.invoke(
        cli,
        "data explain journal_nodes",
        env={"KIARA_DATA_STORE": presseeded_data_store_minimal.config.data_store},
    )

    assert "Latitude" in result.stdout
    assert "arrow_type_name" in result.stdout


# async def test_data_explain_subcommand(presseeded_data_store: Kiara):
#
#     runner = CliRunner()
#     result = await runner.invoke(
#         cli,
#         "data explain journal_nodes",
#         env={"KIARA_DATA_STORE": presseeded_data_store.config.data_store},
#     )
#     assert result.exit_code == 0
#
#     assert "table" in result.stdout
#
#
# async def test_data_load_subcommand(presseeded_data_store: Kiara):
#
#     runner = CliRunner()
#     result = await runner.invoke(
#         cli,
#         "data load journal_nodes",
#         env={"KIARA_DATA_STORE": presseeded_data_store.config.data_store},
#     )
#     assert result.exit_code == 0
#     assert "Id" in result.stdout
#     assert "City" in result.stdout
