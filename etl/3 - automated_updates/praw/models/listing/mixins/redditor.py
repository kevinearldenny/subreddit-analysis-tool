"""Provide the RedditorListingMixin class."""
from typing import Any, Dict, Generator, TypeVar, Union
from urllib.parse import urljoin

from ....util.cache import cachedproperty
from ..generator import ListingGenerator
from .base import BaseListingMixin
from .gilded import GildedListingMixin

Reddit = TypeVar("Reddit")


class SubListing(BaseListingMixin):
    """Helper class for generating :class:`.ListingGenerator` objects."""

    def __init__(self, reddit: Reddit, base_path: str, subpath: str):
        """Initialize a SubListing instance.

        :param reddit: An instance of :class:`.Reddit`.
        :param base_path: The path to the object up to this point.
        :param subpath: The additional path to this sublisting.

        """
        super().__init__(reddit, _data=None)
        self._listing_use_sort = True
        self._reddit = reddit
        self._path = urljoin(base_path, subpath)


class RedditorListingMixin(BaseListingMixin, GildedListingMixin):
    """Adds additional methods pertaining to Redditor instances."""

    @cachedproperty
    def comments(self) -> SubListing:
        r"""Provide an instance of :class:`.SubListing` for comment access.

        For example, to output the first line of all new comments by
        ``/u/spez`` try:

        .. code-block:: python

           for comment in reddit.redditor('spez').comments.new(limit=None):
               print(comment.body.split('\n', 1)[0][:79])

        """
        return SubListing(self._reddit, self._path, "comments")

    @cachedproperty
    def submissions(self) -> SubListing:
        """Provide an instance of :class:`.SubListing` for submission access.

        For example, to output the title's of top 100 of all time submissions
        for ``/u/spez`` try:

        .. code-block:: python

           for submission in reddit.redditor('spez').submissions.top('all'):
               print(submission.title)

        """
        return SubListing(self._reddit, self._path, "submitted")

    def downvoted(
        self, **generator_kwargs: Union[str, int, Dict[str, str]]
    ) -> Generator[Any, None, None]:
        """Return a :class:`.ListingGenerator` for items the user has downvoted.

        May raise ``prawcore.Forbidden`` after issuing the request if the user
        is not authorized to access the list. Note that because this function
        returns a :class:`.ListingGenerator` the exception may not occur until
        sometime after this function has returned.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get all downvoted items of the authenticated user:

        .. code-block:: python

            for item in reddit.user.me().downvoted():
                print(item.id)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "downvoted"), **generator_kwargs
        )

    def gildings(
        self, **generator_kwargs: Union[str, int, Dict[str, str]]
    ) -> Generator[Any, None, None]:
        """Return a :class:`.ListingGenerator` for items the user has gilded.

        May raise ``prawcore.Forbidden`` after issuing the request if the user
        is not authorized to access the list. Note that because this function
        returns a :class:`.ListingGenerator` the exception may not occur until
        sometime after this function has returned.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get all gilded items of the authenticated user:

        .. code-block:: python

            for item in reddit.user.me().gildings():
                print(item.id)

        """
        return ListingGenerator(
            self._reddit,
            urljoin(self._path, "gilded/given"),
            **generator_kwargs
        )

    def hidden(
        self, **generator_kwargs: Union[str, int, Dict[str, str]]
    ) -> Generator[Any, None, None]:
        """Return a :class:`.ListingGenerator` for items the user has hidden.

        May raise ``prawcore.Forbidden`` after issuing the request if the user
        is not authorized to access the list. Note that because this function
        returns a :class:`.ListingGenerator` the exception may not occur until
        sometime after this function has returned.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get all hidden items of the authenticated user:

        .. code-block:: python

            for item in reddit.user.me().hidden():
                print(item.id)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "hidden"), **generator_kwargs
        )

    def saved(
        self, **generator_kwargs: Union[str, int, Dict[str, str]]
    ) -> Generator[Any, None, None]:
        """Return a :class:`.ListingGenerator` for items the user has saved.

        May raise ``prawcore.Forbidden`` after issuing the request if the user
        is not authorized to access the list. Note that because this function
        returns a :class:`.ListingGenerator` the exception may not occur until
        sometime after this function has returned.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get all saved items of the authenticated user:

        .. code-block:: python

            for item in reddit.user.me().saved():
                print(item.id)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "saved"), **generator_kwargs
        )

    def upvoted(
        self, **generator_kwargs: Union[str, int, Dict[str, str]]
    ) -> Generator[Any, None, None]:
        """Return a :class:`.ListingGenerator` for items the user has upvoted.

        May raise ``prawcore.Forbidden`` after issuing the request if the user
        is not authorized to access the list. Note that because this function
        returns a :class:`.ListingGenerator` the exception may not occur until
        sometime after this function has returned.

        Additional keyword arguments are passed in the initialization of
        :class:`.ListingGenerator`.

        For example, to get all upvoted items of the authenticated user:

        .. code-block:: python

            for item in reddit.user.me().upvoted():
                print(item.id)

        """
        return ListingGenerator(
            self._reddit, urljoin(self._path, "upvoted"), **generator_kwargs
        )