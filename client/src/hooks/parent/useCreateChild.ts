import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { UseMutationResult, useMutation, useQueryClient } from 'react-query';
import { Child, ChildRequest } from 'types/generated';

export default function useCreateChild(): UseMutationResult<
  AxiosResponse<Child>,
  AxiosError<{ message: string }>,
  ChildRequest
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const postChild = (payload: ChildRequest) => {
    return client.post(`parents/children`, payload);
  };

  return useMutation(postChild, {
    onSuccess: () => {
      queryClient.invalidateQueries(['children']);
    },
  });
}
