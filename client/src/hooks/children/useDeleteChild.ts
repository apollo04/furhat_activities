import { AxiosError, AxiosResponse } from 'axios';
import { useMutation, UseMutationResult, useQueryClient } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useDeleteChild(): UseMutationResult<
  AxiosResponse<void>,
  AxiosError<{ message: string }>,
  string
> {
  const queryClient = useQueryClient();

  const deleteChild = (childId: string) => {
    return axiosUnauthorizedInstance.delete(`/children/${childId}/`);
  };

  return useMutation(deleteChild, {
    onSuccess: () => {
      queryClient.invalidateQueries(['children']);
    },
  });
}
