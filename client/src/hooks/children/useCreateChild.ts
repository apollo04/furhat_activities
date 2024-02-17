import { AxiosError, AxiosResponse } from 'axios';
import { UseMutationResult, useMutation, useQueryClient } from 'react-query';
import { Child, ChildRequest } from 'types/generated';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useCreateChild(): UseMutationResult<
  AxiosResponse<Child>,
  AxiosError<{ message: string }>,
  ChildRequest
> {
  const queryClient = useQueryClient();

  const postChild = (payload: ChildRequest) => {
    return axiosUnauthorizedInstance.post(`/children/`, payload);
  };

  return useMutation(postChild, {
    onSuccess: () => {
      queryClient.invalidateQueries(['children']);
    },
  });
}
