import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { UseMutationResult, useMutation, useQueryClient } from 'react-query';
import { Center, CenterRequest } from 'types/generated';

export default function useCreateCenter(): UseMutationResult<
  AxiosResponse<Center>,
  AxiosError<{ message: string }>,
  CenterRequest
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const postCenter = (payload: CenterRequest) => {
    return client.post(`admins/center`, payload);
  };

  return useMutation(postCenter, {
    onSuccess: () => {
      queryClient.invalidateQueries(['centers']);
    },
  });
}
