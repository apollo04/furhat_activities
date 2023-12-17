import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useMutation, UseMutationResult, useQueryClient } from 'react-query';

export default function useDeleteChild(): UseMutationResult<
  AxiosResponse<void>,
  AxiosError<{ message: string }>,
  string
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const deleteChild = (childId: string) => {
    return client.delete(`parents/children/${childId}/`);
  };

  return useMutation(deleteChild, {
    onSuccess: () => {
      queryClient.invalidateQueries(['children']);
    },
  });
}
