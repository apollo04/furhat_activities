import { AxiosError, AxiosResponse } from 'axios';
import { useClient } from 'contexts/AuthContext';
import { useMutation, UseMutationResult, useQueryClient } from 'react-query';
import { Child, ChildRequest } from 'types/generated';

export default function useUpdateChild(
  childId?: string,
): UseMutationResult<
  AxiosResponse<Child>,
  AxiosError<{ message: string }>,
  ChildRequest
> {
  const client = useClient();
  const queryClient = useQueryClient();

  const updateChild = (payload: ChildRequest) => {
    return client.patch(`parents/children/${childId}/`, payload);
  };

  return useMutation(updateChild, {
    onSuccess: () => {
      queryClient.invalidateQueries(['children']);
    },
  });
}
