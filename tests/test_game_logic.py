import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_winning_guess_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_winning_guess_boundary_high():
    outcome, _ = check_guess(200, 200)
    assert outcome == "Win"

def test_guess_one_below_secret():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_guess_one_above_secret():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_valid_float_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5


# --- get_range_for_difficulty ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200

def test_hard_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_unknown_difficulty_defaults():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# --- update_score ---

def test_win_on_first_attempt():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*1

def test_win_score_decreases_with_attempts():
    score_early = update_score(0, "Win", 2)
    score_late = update_score(0, "Win", 5)
    assert score_early > score_late

def test_win_score_minimum_10():
    # attempt 10 would give 100 - 100 = 0, but capped at 10
    score = update_score(0, "Win", 10)
    assert score == 10

def test_too_low_deducts_score():
    score = update_score(50, "Too Low", 3)
    assert score == 45

def test_too_high_even_attempt_adds_score():
    score = update_score(50, "Too High", 2)
    assert score == 55

def test_too_high_odd_attempt_deducts_score():
    score = update_score(50, "Too High", 3)
    assert score == 45

def test_unknown_outcome_unchanged():
    score = update_score(50, "SomeOtherOutcome", 1)
    assert score == 50
