import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useMutation, UseMutationResult, useQueryClient } from 'react-query';
import { Center, CenterRequest } from 'types/generated';

export default function useUpdateCenter(
  centerId?: string,
): UseMutationResult<
  AxiosResponse<Center>,
  AxiosError<{ message: string }>,
  CenterRequest
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const updateCenter = (payload: CenterRequest) => {
    return client.patch(`admins/center/${centerId}/`, payload);
  };

  return useMutation(updateCenter, {
    onSuccess: () => {
      queryClient.invalidateQueries(['centers']);
    },
  });
}
