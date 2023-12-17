import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useMutation, UseMutationResult, useQueryClient } from 'react-query';

export default function useDeleteCenter(): UseMutationResult<
  AxiosResponse<void>,
  AxiosError<{ message: string }>,
  string
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const deleteCenter = (centerId: string) => {
    return client.delete(`admins/center/${centerId}/`);
  };

  return useMutation(deleteCenter, {
    onSuccess: () => {
      queryClient.invalidateQueries(['centers']);
    },
  });
}
