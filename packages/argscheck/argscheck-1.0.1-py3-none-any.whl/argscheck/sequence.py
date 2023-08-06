"""
Sequences
=========

This module contains checkers for sequence objects.

In this context, a sequence is a class that:

1. Has ``__len__()`` implemented.
2. Has ``__getitem__()`` implemented, which accepts integers starting from zero and up to (and not including) the
   object's own length.
3. Can be instantiated from an iterable.

Moreover, a mutable sequence is a class that:

1. Has the properties of a sequence.
2. Has ``__setitem__()`` implemented, which accepts the same keys as ``__getitem__()``.

Sequences (mutable or otherwise) can be homogeneous, i.e. all items in it have some shared properties. Homogeneity can
be checked using the ``*args`` parameter:

If a non-empty ``*args`` is provided, then, the resulting checker is applied to each item in the sequence.

Checkers that convert values (like :class:`.Optional` for example) are applied as follows:

1. For mutable sequences, converted items are set inplace.
2. For (non mutable) sequences, a new sequence instance is created from the converted items (this will happen only if
   actual conversion took place for at least one item).
"""
from .core import Checker, Typed
from .numeric import Sized, NonEmpty


class Sequence(Sized, Typed):
    """
    Check if ``x`` is a sequence.

    :Example:

    .. code-block:: python

        from argscheck import Sequence

        # Check if a set of length at least 2
        checker = Sequence(str, len_ge=2)

        checker.check(['a', 'b'])    # Passes, returns ['a', 'b']
        checker.check({'a', 'b'})    # Fails, raises TypeError (set is not a sequence)
        checker.check(['a'])         # Fails, raises ValueError (length is less than 2)
        checker.check(['a', 1])      # Fails, raises TypeError (not all items are str)

    """
    types = (object,)

    def __init__(self, *args, **kwargs):
        super().__init__(*self.types, **kwargs)

        if args:
            self.item_checker = Checker.from_checker_likes(args)
        else:
            self.item_checker = None

    def _get_items(self, name, value):
        items = []
        modified = False

        item_name, seq_name = ((name + '[{}]', name)
                               if name
                               else ('sequence item {}', 'it'))

        # Get length
        try:
            length = len(value)
        except TypeError:
            return False, TypeError(f'Failed calling len(), make sure {seq_name} is a sequence.'), modified

        # Form a list of returned items by getting each item by its integer index, and applying the item checker on it
        for i in range(length):
            try:
                pre_check_item = value[i]
            except TypeError:
                return False, TypeError(f'Failed getting {item_name.format(i)}, make sure {seq_name} is a sequence.'), \
                       modified

            passed, post_check_item = self.item_checker(item_name.format(i), pre_check_item)
            if not passed:
                return False, post_check_item, modified

            if post_check_item is not pre_check_item:
                modified = True

            items.append(post_check_item)

        return True, items, modified

    def _set_items(self, name, value, items):
        # Create a new sequence of the same type, with the modified items
        try:
            return True, type(value)(items)
        except TypeError:
            return False, TypeError(f'Failed on {type(value).__qualname__}(), make sure this type can be instantiated '
                                    f'from an iterable.')

    def __call__(self, name, value):
        passed, value = super().__call__(name, value)
        if not passed:
            return False, value

        # If Sequence was constructed with an empty *args, no need to iterate over items in the sequence
        if self.item_checker is None:
            return True, value

        # Get all items in the sequence, check (and possibly convert) each one, arrange them in a list
        passed, items, modified = self._get_items(name, value)
        if not passed:
            return False, items

        # If none of the items were modified, can return now without setting them
        if not modified:
            return True, value

        # Prepare return value. For an immutable sequence, a new sequence instance is created and returned, for a
        # mutable sequence, items are set inplace and the original sequence is returned.
        passed, value = self._set_items(name, value, items)
        if not passed:
            return False, value

        return True, value


class NonEmptySequence(NonEmpty, Sequence):
    """
    Same as :class:`.Sequence`, plus, the length of ``x`` must be greater than zero.

    :meta skip-extend-docstring:
    """
    pass


class Tuple(Sequence):
    """
    Same as :class:`.Sequence`, plus, ``x`` must be a ``tuple``.

    :meta skip-extend-docstring:
    """
    types = (tuple,)


class NonEmptyTuple(NonEmpty, Tuple):
    """
    Same as :class:`.Tuple`, plus, the length of ``x`` must be greater than zero.

    :meta skip-extend-docstring:
    """
    pass


class MutableSequence(Sequence):
    """
    Check if ``x`` is a mutable sequence.

    """
    def _set_items(self, name, value, items):
        item_name, seq_name = ((name + '[{}]', name)
                               if name
                               else ('sequence item {}', 'it'))

        # Iterate over checked items, set each one to the mutable sequence by its integer index
        for i, item in enumerate(items):
            try:
                value[i] = item
            except TypeError:
                return False, TypeError(f'Failed setting {item_name.format(i)}, make sure {seq_name} is a mutable '
                                        f'sequence.')

        return True, value


class NonEmptyMutableSequence(NonEmpty, MutableSequence):
    """
    Same as :class:`.MutableSequence`, plus, the length of ``x`` must be greater than zero.

    :meta skip-extend-docstring:
    """
    pass


class List(MutableSequence):
    """
    Same as :class:`.MutableSequence`, plus, ``x`` must be a ``list``.

    :meta skip-extend-docstring:
    """
    types = (list,)


class NonEmptyList(NonEmpty, List):
    """
    Same as :class:`.List`, plus, the length of ``x`` must be greater than zero.

    :meta skip-extend-docstring:
    """
    pass
