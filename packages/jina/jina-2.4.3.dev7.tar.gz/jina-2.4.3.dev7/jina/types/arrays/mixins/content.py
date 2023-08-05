from typing import List, Sequence, TYPE_CHECKING

from ...ndarray import NdArray

if TYPE_CHECKING:
    from ...document import ArrayType


class ContentPropertyMixin:
    """Helpers that provide faster getter & setter for :attr:`.content` by using protobuf directly. """

    def _check_length(self, target_len: int):
        if target_len != len(self):
            raise ValueError(
                f'Length must match {self!r}, but {target_len} != {len(self)}'
            )

    @property
    def embeddings(self) -> 'ArrayType':
        """Return a :class:`ArrayType` stacking all the `embedding` attributes as rows.

        :return: a :class:`ArrayType` of embedding
        """
        return NdArray.unravel([d.embedding for d in self._pb_body])

    @embeddings.setter
    def embeddings(self, value: 'ArrayType'):
        """Set the :attr:`.embedding` of the Documents.

        To remove all embeddings of all Documents:
        .. highlight:: python
        .. code-block:: python

            da.embeddings = None

        :param value: The embedding matrix to set
        """

        if value is None:
            for d in self._pb_body:
                d.ClearField('embedding')
        else:
            emb_shape0 = value.shape[0]
            self._check_length(emb_shape0)
            NdArray.ravel(value, self, 'embedding')

    @property
    def blobs(self) -> 'ArrayType':
        """Return a :class:`ArrayType` stacking all :attr:`.blob`.

        The `blob` attributes are stacked together along a newly created first
        dimension (as if you would stack using ``np.stack(X, axis=0)``).

        .. warning:: This operation assumes all blobs have the same shape and dtype.
                 All dtype and shape values are assumed to be equal to the values of the
                 first element in the DocumentArray / DocumentArrayMemmap

        :return: a :class:`ArrayType` of blobs
        """
        return NdArray.unravel([d.blob for d in self._pb_body])

    @blobs.setter
    def blobs(self, value: 'ArrayType'):
        """Set :attr:`.blob` of the Documents. To clear all :attr:`blob`, set it to ``None``.

        :param value: The blob array to set. The first axis is the "row" axis.
        """

        if value is None:
            for d in self._pb_body:
                d.ClearField('blob')
        else:
            blobs_shape0 = value.shape[0]
            self._check_length(blobs_shape0)

            NdArray.ravel(value, self, 'blob')

    @property
    def texts(self) -> List[str]:
        """Get :attr:`.text` of all Documents

        :return: a list of texts
        """
        return [d.text for d in self._pb_body]

    @texts.setter
    def texts(self, value: Sequence[str]):
        """Set :attr:`.text` for all Documents. To clear all :attr:`text`, set it to ``None``.

        :param value: A sequence of texts to set, should be the same length as the
            number of Documents
        """
        if value is None:
            for d in self._pb_body:
                d.ClearField('text')
        else:
            self._check_length(len(value))

            for doc, text in zip(self._pb_body, value):
                doc.text = text

    @property
    def buffers(self) -> List[bytes]:
        """Get the buffer attribute of all Documents.

        :return: a list of buffers
        """
        return [d.buffer for d in self._pb_body]

    @buffers.setter
    def buffers(self, value: List[bytes]):
        """Set the buffer attribute for all Documents. To clear all :attr:`buffer`, set it to ``None``.

        :param value: A sequence of buffer to set, should be the same length as the
            number of Documents
        """

        if value is None:
            for d in self._pb_body:
                d.ClearField('buffer')
        else:
            self._check_length(len(value))

            for doc, buffer in zip(self._pb_body, value):
                doc.buffer = buffer
