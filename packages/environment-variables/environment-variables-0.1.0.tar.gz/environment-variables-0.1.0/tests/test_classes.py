import pytest

from src.environment_variables import EnvVarMeta, EnvVars, environment_variables
from src.environment_variables.exceptions import (
    EnvironmentValidationError,
    EnvironmentVariableTypeError,
)


class EnvironmentWithMeta(metaclass=EnvVarMeta):
    BOOLEAN_TRUE: bool
    BOOLEAN_FALSE: bool
    BOOLEAN_TRUE_AS_INT: bool
    BOOLEAN_FALSE_AS_INT: bool
    STRING_VALUE: str
    FLOAT_VALUE: float
    INTEGER_VALUE: int


class EnvironmentWithInheritance(EnvVars):
    BOOLEAN_TRUE: bool
    BOOLEAN_FALSE: bool
    BOOLEAN_TRUE_AS_INT: bool
    BOOLEAN_FALSE_AS_INT: bool
    STRING_VALUE: str
    FLOAT_VALUE: float
    INTEGER_VALUE: int


@environment_variables
class EnvironmentWithDecorator:
    BOOLEAN_TRUE: bool
    BOOLEAN_FALSE: bool
    BOOLEAN_TRUE_AS_INT: bool
    BOOLEAN_FALSE_AS_INT: bool
    STRING_VALUE: str
    FLOAT_VALUE: float
    INTEGER_VALUE: int


@environment_variables()
class EnvironmentWithDecoratorAndParenthesis:
    BOOLEAN_TRUE: bool
    BOOLEAN_FALSE: bool
    BOOLEAN_TRUE_AS_INT: bool
    BOOLEAN_FALSE_AS_INT: bool
    STRING_VALUE: str
    FLOAT_VALUE: float
    INTEGER_VALUE: int


@pytest.fixture(
    params=[
        EnvironmentWithMeta,
        EnvironmentWithInheritance,
        EnvironmentWithDecorator,
        EnvironmentWithDecoratorAndParenthesis,
    ]
)
def env_class(request):
    return request.param


def test_get_boolean_true(env_class):
    assert env_class.BOOLEAN_TRUE
    assert isinstance(env_class.BOOLEAN_TRUE, bool)


def test_get_boolean_false(env_class):
    assert not env_class.BOOLEAN_FALSE
    assert isinstance(env_class.BOOLEAN_FALSE, bool)


def test_get_boolean_true_from_int(env_class):
    assert env_class.BOOLEAN_TRUE_AS_INT
    assert isinstance(env_class.BOOLEAN_TRUE_AS_INT, bool)


def test_get_boolean_false_from_int(env_class):
    assert not env_class.BOOLEAN_FALSE_AS_INT
    assert isinstance(env_class.BOOLEAN_FALSE_AS_INT, bool)


def test_get_string(environment_variables, env_class):
    assert environment_variables.get('STRING_VALUE') == env_class.STRING_VALUE
    assert isinstance(env_class.STRING_VALUE, str)


def test_get_float(environment_variables, env_class):
    assert float(environment_variables.get('FLOAT_VALUE')) == env_class.FLOAT_VALUE
    assert isinstance(env_class.FLOAT_VALUE, float)


def test_get_integer(environment_variables, env_class):
    assert int(environment_variables.get('INTEGER_VALUE')) == env_class.INTEGER_VALUE
    assert isinstance(env_class.INTEGER_VALUE, int)


def test_can_not_access_variable_that_is_not_defined(env_class):
    with pytest.raises(AttributeError):
        _ = env_class.IS_NOT_DEFINED


def test_can_not_cast_variable_if_type_is_not_matching():
    class TypeMismatch:
        STRING_VALUE: int

    env_class = environment_variables(TypeMismatch)
    with pytest.raises(EnvironmentVariableTypeError):
        _ = env_class.STRING_VALUE


def test_if_prefix_is_specified_the_class_finds_all_matching_variables():
    @environment_variables(collect_prefixes=['DEFINED'])
    class AutomaticEnvironment:
        DEFINED_FLOAT_VALUE: float
        DEFINED_INTEGER_VALUE: int

    assert 'true' == AutomaticEnvironment.DEFINED_BOOLEAN_TRUE
    assert 'false' == AutomaticEnvironment.DEFINED_BOOLEAN_FALSE
    assert 'STRING_VALUE' == AutomaticEnvironment.DEFINED_STRING_VALUE
    assert 10.001 == AutomaticEnvironment.DEFINED_FLOAT_VALUE
    assert 19 == AutomaticEnvironment.DEFINED_INTEGER_VALUE


def test_validate_environment_variables_raises_no_errors_if_all_is_valid():
    try:

        @environment_variables(validate=True)
        class ValidateEnvironment:
            BOOLEAN_TRUE: bool
            STRING_VALUE: str
            INTEGER_VALUE: int
            FLOAT_VALUE: float
            DOES_NOT_EXIST: str = 'default'

    except EnvironmentValidationError:
        pytest.fail()


def test_validate_environment_raises_error_if_environment_variable_is_not_defined():
    with pytest.raises(EnvironmentValidationError):

        @environment_variables(validate=True)
        class ValidateEnvironment:
            DOES_NOT_EXIST: bool


def test_validate_environment_raises_error_if_env_var_can_not_be_cast():
    with pytest.raises(EnvironmentValidationError):

        @environment_variables(validate=True)
        class ValidateEnvironment:
            STRING_VALUE: float
